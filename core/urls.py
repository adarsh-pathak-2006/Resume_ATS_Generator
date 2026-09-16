from django.urls import path
from .views import ResumeAPI, ResumeAnalyzeListAPI, ResumeAnalyseDetailAPI, ResumeAnalysePostAPI, ResumeDetailAPI

urlpatterns = [
    path('resume/', ResumeAPI.as_view()),
    path('resume/<int:pk>/', ResumeDetailAPI.as_view()),
    path('resume-analyse/<int:pk>/', ResumeAnalysePostAPI.as_view()),
    path('analysis/', ResumeAnalyzeListAPI.as_view()),
    path('analysis/<int:pk>/', ResumeAnalyseDetailAPI.as_view()),
]
