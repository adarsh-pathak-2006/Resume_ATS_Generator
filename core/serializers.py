from rest_framework.serializers import ModelSerializer
from .models import Resume, ResponseDatabase

class ResumeSerializer(ModelSerializer):
    class Meta:
        model=Resume
        fields='__all__'
        read_only_fields=['added_on']

class ResumeUploadSerializer(ModelSerializer):
    class Meta:
        model=ResponseDatabase
        fields='__all__'
        read_only_fields=['generated_resume', 'cover_letter', 'created_on']