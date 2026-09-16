from ai import get_response
from ai_prompt import prompt_generate_resume, prompt_genrate_resume_with_coverletter

async def get_resume_response(resume, jd):
    prompt=prompt_generate_resume(main_resume=resume, jd=jd)
    response=await get_response(prompt=prompt)
    return response

async def get_resumeandcoverletter_response(resume, jd, companyinfo):
    prompt=prompt_genrate_resume_with_coverletter(main_resume=resume, jd=jd, company_info=companyinfo)
    response=await get_response(prompt=prompt)
    return {'resume':response.get('resume'), 'cover_letter':response.get('cover_letter')}