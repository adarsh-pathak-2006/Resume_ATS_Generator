from google import genai
from django.conf import settings

from google.genai import types

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def get_response(prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )
    return response