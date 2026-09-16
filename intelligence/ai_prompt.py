def prompt_generate_resume(main_resume, jd):
    return f"""You are an expert ATS (Applicant Tracking System) optimizer and professional resume writer.
I will provide you with a candidate's current resume and a target job description. 
Your task is to completely rewrite and optimize the resume to maximize its ATS score and appeal to recruiters for this specific role.

Current Resume:
{main_resume}

Target Job Description:
{jd}

Instructions:
1. Extract the most relevant skills, keywords, and experiences from the JD and naturally weave them into the resume.
2. Rewrite bullet points to be impact-driven (e.g., using the X-Y-Z formula: Accomplished [X] as measured by [Y], by doing [Z]).
3. Ensure the formatting is clean, professional, and standard markdown (use headers, bullet points, bold text).
4. Do not lie or invent experience that the candidate does not have; reframe existing experience to highlight relevance.
5. Format the final output strictly as Markdown.
"""

def prompt_genrate_resume_with_coverletter(main_resume, jd, company_info):
    return f"""You are an expert ATS (Applicant Tracking System) optimizer, professional resume writer, and career coach.
I will provide you with a candidate's current resume, a target job description, and information about the company.
Your task is to generate a highly optimized resume AND a compelling, tailored cover letter.

Current Resume:
{main_resume}

Target Job Description:
{jd}

Company Information:
{company_info}

Instructions for Resume:
1. Extract the most relevant keywords from the JD and naturally weave them into the resume.
2. Rewrite bullet points to be impact-driven (using quantifiable metrics where possible).
3. Format strictly as professional Markdown.

Instructions for Cover Letter:
1. Write a 3-4 paragraph cover letter addressed to the Hiring Manager.
2. The tone should be enthusiastic, professional, and confident.
3. Explicitly connect the candidate's past achievements (from the resume) to the specific needs of the role (from the JD) and the company's mission/culture (from the Company Info).
4. Format strictly as professional Markdown.
"""