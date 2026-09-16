from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    resume=models.FileField('resume-pdfs/')
    added_on=models.DateTimeField(auto_now_add=True)

class ResponseDatabase(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    resume=models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_description=models.TextField()
    about_company=models.TextField()
    letter_required=models.BooleanField(default=True)
    generated_resume=models.FileField(upload_to='generated_resume')
    cover_letter=models.TextField(null=True)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_description[:80]

