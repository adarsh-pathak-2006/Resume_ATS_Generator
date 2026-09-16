from django.shortcuts import get_object_or_404
from .models import ResponseDatabase, Resume
from .serializers import ResumeSerializer, ResumeUploadSerializer
from authentication.serializers import UserGetSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

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


 


