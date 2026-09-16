from .models import ResponseDatabase, Resume
from .serializers import ResumeSerializer, ResumeUploadSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import resume_pdf_to_text
from intelligence.response import get_resume_response, get_resumeandcoverletter_response
from rest_framework.permissions import IsAuthenticated

class ResumeAPI(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ResumeSerializer

    def get_queryset(self):
        return Resume.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResumeDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ResumeSerializer

    def get_queryset(self):
        return Resume.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    

class ResumeAnalyzeListAPI(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ResumeUploadSerializer

    def get_queryset(self):
        return ResponseDatabase.objects.select_related('user', 'resume').filter(user=self.request.user)

class ResumeAnalyseDetailAPI(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ResumeUploadSerializer
    def get_queryset(self):
        return ResponseDatabase.objects.select_related('user', 'resume').filter(user=self.request.user)

class ResumeUploadAPI(APIView):
    permission_classes=[IsAuthenticated]
    async def post(self, request, pk):
        serial=ResumeUploadSerializer(data=request.data)
        if serial.is_valid():
            jd=serial.validated_data['job_description']
            about_company=serial.validated_data['about_company']
            is_cover_letter_required=serial.validated_data.get("letter_requrired")
            resume_data=resume_pdf_to_text.delay(pk)
            if not is_cover_letter_required:
                output=await get_resume_response(resume=resume_data, jd=jd)
            else:
                output=await get_resumeandcoverletter_response(resume=resume_data, jd=jd, companyinfo=about_company)
            serial.save(user=request.user, generated_resume=output.get('resume'), cover_letter=output.get('cover_letter'))
            return Response({'output':output}, status=201)
        return Response(serial.errors, status=400)