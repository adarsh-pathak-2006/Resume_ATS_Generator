from .ai import get_response
from .ai_prompt import prompt_generate_resume, prompt_genrate_resume_with_coverletter

import json

def get_resume_response(resume, jd):
    prompt=prompt_generate_resume(main_resume=resume, jd=jd)
    prompt += "\n\nPlease respond in valid JSON format with a single key 'resume'."
    response=get_response(prompt=prompt)
    try:
        return json.loads(response.text)
    except Exception:
        return {'resume': response.text}

def get_resumeandcoverletter_response(resume, jd, companyinfo):
    prompt=prompt_genrate_resume_with_coverletter(main_resume=resume, jd=jd, company_info=companyinfo)
    prompt += "\n\nPlease respond in valid JSON format with keys 'resume' and 'cover_letter'."
    response=get_response(prompt=prompt)
    try:
        return json.loads(response.text)
    except Exception:
        return {'resume': response.text, 'cover_letter': ''}