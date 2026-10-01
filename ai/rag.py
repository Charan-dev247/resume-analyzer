import os
import json

from dotenv import load_dotenv
from groq import Groq


# Load variables from .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")


client = Groq(api_key=api_key)


def generate_rag_analysis(resume_chunks, job_description):
    """
    Generate an AI-powered resume/job analysis using
    retrieved resume chunks and the job description.
    """

    # Combine retrieved chunks into context
    context = "\n\n".join(
        f"RESUME SECTION {i + 1}:\n{chunk}"
        for i, chunk in enumerate(resume_chunks)
    )

    prompt = f"""
You are an AI recruitment assistant.

Analyze the candidate's resume against the job description.

Use ONLY the information provided below.
Do not invent skills, experience, education, or projects.

JOB DESCRIPTION:
{job_description}

RELEVANT RESUME SECTIONS:
{context}

Provide:

1. Overall match score from 0 to 100
2. Skills that match the job
3. Skills that are missing or not demonstrated
4. Relevant candidate experience
5. Important skill gaps
6. Specific recommendations to improve the candidate's fit

Return ONLY valid JSON using exactly this structure:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "relevant_experience": [],
    "skill_gaps": [],
    "recommendations": []
}}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise AI recruitment assistant. "
                    "Return only valid JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        response_format={"type": "json_object"}
    )

    result = response.choices[0].message.content

    return json.loads(result)