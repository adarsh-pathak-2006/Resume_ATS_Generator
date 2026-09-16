from django.shortcuts import get_object_or_404
from .models import ResponseDatabase, Resume
from .serializers import ResumeSerializer, ResumeUploadSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import resume_pdf_to_text
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

class ResumeAnalysePostAPI(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, pk):
        serial=ResumeUploadSerializer(data=request.data)
        if serial.is_valid():
            jd=serial.validated_data['job_description']
            about_company=serial.validated_data['about_company']
            is_cover_letter_required=serial.validated_data.get("letter_required")
            data=ResponseDatabase.objects.create(user=request.user, resume=get_object_or_404(Resume, id=pk), job_description=jd, about_company=about_company, letter_required=is_cover_letter_required)
            output=resume_pdf_to_text.delay(data_id=data.id)
            return Response({'message': 'Processing in background', 'task_id': output.id, 'analysis_id': data.id}, status=202)
        return Response(serial.errors, status=400)