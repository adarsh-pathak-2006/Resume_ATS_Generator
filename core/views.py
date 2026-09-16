from .models import ResponseDatabase, Resume
from .serializers import ResumeSerializer, ResumeUploadSerializer, ResumeDetailGetSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import resume_pdf_to_text
from intelligence.response import get_resume_response, get_resumeandcoverletter_response

class ResumeAPI(ListCreateAPIView):
    serializer_class=ResumeSerializer

    def get_queryset(self):
        return Resume.objects.select_related('user').filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResumeAnalyzeListAPI(ListAPIView):
    serializer_class=ResumeUploadSerializer

    def get_queryset(self):
        return ResponseDatabase.objects.select_related('user', 'resume').filter(user=self.request.user)

class ResumeAnalyseDetailAPI(RetrieveAPIView):
    serializer_class=ResumeDetailGetSerializer
    def get_queryset(self):
        return ResponseDatabase.objects.select_related('user', 'resume').filter(user=self.request.user)

class ResumeUploadAPI(APIView):
    async def post(self, request):
        serial=ResumeUploadSerializer(data=request.data)
        if serial.is_valid():
            resume_id=serial.validated_data['resume']
            jd=serial.validated_data['job_description']
            about_company=serial.validated_data['about_company']
            is_cover_letter_required=serial.validated_data.get("letter_requrired")
            resume_data=resume_pdf_to_text.delay(resume_id)
            if not is_cover_letter_required:
                output=await get_resume_response(resume=resume_data, jd=jd)
            else:
                output=await get_resumeandcoverletter_response(resume=resume_data, jd=jd, companyinfo=about_company)
            serial.save(user=request.user, generated_resume=output.get('resume'), cover_letter=output.get('cover_letter'))
            return Response({'output':output}, status=201)
        return Response(serial.errors, status=400)