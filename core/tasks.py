from django.shortcuts import get_object_or_404
from intelligence.response import get_resume_response, get_resumeandcoverletter_response
from celery import shared_task
import pymupdf
from core.models import Resume

@shared_task
def resume_pdf_to_text(resumeid, required, jd, about_company):
    resume_data=get_object_or_404(Resume, id=resumeid)
    doc = pymupdf.open(resume_data.resume)
    resume=''
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        data = page.get_text()
        resume=resume+data
    if not required:
        output=get_resume_response(resume=resume_data, jd=jd)
    else:
        output=get_resumeandcoverletter_response(resume=resume_data, jd=jd, companyinfo=about_company)
    return output

    