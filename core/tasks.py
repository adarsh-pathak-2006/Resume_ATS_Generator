from django.shortcuts import get_object_or_404
from intelligence.response import get_resume_response, get_resumeandcoverletter_response
from celery import shared_task
import pymupdf
from .models import ResponseDatabase

@shared_task
def resume_pdf_to_text(data_id):
    saved=get_object_or_404(ResponseDatabase, id=data_id)
    doc = pymupdf.open(saved.resume.path)
    resume=''
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        data = page.get_text()
        resume=resume+data
    if not saved.letter_required:
        output_response=get_resume_response(resume=resume, jd=saved.job_description)
    else:
        output_response=get_resumeandcoverletter_response(resume=resume, jd=saved.job_description, companyinfo=saved.about_company)
    saved.generated_resume=output_response.get('resume')
    saved.cover_letter=output_response.get('cover_letter')
    saved.save()
    return {'resume':output_response.get('resume'), 'cover_letter':output_response.get('cover_letter')}

    