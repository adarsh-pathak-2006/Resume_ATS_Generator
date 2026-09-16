from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Resume, ResponseDatabase
from authentication.serializers import UserGetSerializer

class ResumeSerializer(ModelSerializer):
    user=UserGetSerializer(read_only=True)
    class Meta:
        model=Resume
        fields='__all__'
        read_only_fields=['added_on']

class ResumeUploadSerializer(ModelSerializer):
    resume=PrimaryKeyRelatedField(queryset=Resume.objects.select_related('user').all())
    user=UserGetSerializer(read_only=True)
    class Meta:
        model=ResponseDatabase
        fields='__all__'
        read_only_fields=['generated_resume', 'cover_letter', 'created_on']