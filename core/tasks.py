from django.shortcuts import get_object_or_404
from celery import shared_task
import pymupdf
from core.models import Resume

@shared_task
def resume_pdf_to_text(resumeid):
    resume_data=get_object_or_404(Resume, id=resumeid)
    doc = pymupdf.open(resume_data.resume)
    text=''
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        data = page.get_text()
        text=text+data
    return text
    