from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def evaluate_candidate(
    job_description,
    candidate
):

    candidate_document = candidate.get(
        "document",
        ""
    )[:4000]

    prompt = f"""
You are a senior AI recruiter.

Your task is to evaluate candidates for an AI Engineer role.

Strongly prioritize:

- AI Engineering experience
- Machine Learning experience
- NLP experience
- LLM Fine-Tuning
- RAG systems
- LangChain
- MLOps
- Generative AI projects
- AI Research work
- Production AI systems

Give HIGHER scores to candidates with titles such as:

- AI Engineer
- ML Engineer
- NLP Engineer
- AI Research Engineer
- Data Scientist
- Machine Learning Scientist

Give LOWER scores to candidates with titles such as:

- DevOps Engineer
- Cloud Engineer
- Backend Engineer
- Full Stack Developer

UNLESS there is strong evidence of AI/ML work in the profile.

JOB DESCRIPTION:
{job_description}

CANDIDATE PROFILE:
{candidate_document}

CANDIDATE METADATA:

Current Title:
{candidate['metadata'].get('current_title', '')}

Years of Experience:
{candidate['metadata'].get('years_of_experience', 0)}

Industry:
{candidate['metadata'].get('industry', '')}

Recruiter Response Rate:
{candidate['metadata'].get('recruiter_response_rate', 0)}

Interview Completion Rate:
{candidate['metadata'].get('interview_completion_rate', 0)}

GitHub Activity Score:
{candidate['metadata'].get('github_activity_score', 0)}

Open To Work:
{candidate['metadata'].get('open_to_work', False)}

Evaluate:

1. Technical Fit
2. AI/ML Alignment
3. Career Alignment
4. Hiring Potential

Return ONLY valid JSON.

{{
    "fit_score": 0,
    "technical_fit": 0,
    "ai_ml_alignment": 0,
    "career_alignment": 0,
    "recommendation": "Strong Fit"
}}

Rules:

- All scores must be between 0 and 100.
- Return ONLY JSON.
- Do not explain.
- Do not return markdown.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        content = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        match = re.search(
            r"\{.*\}",
            content,
            re.DOTALL
        )

        if match:

            result = json.loads(
                match.group()
            )

            result.setdefault(
                "fit_score",
                50
            )

            result.setdefault(
                "technical_fit",
                50
            )

            result.setdefault(
                "ai_ml_alignment",
                50
            )

            result.setdefault(
                "career_alignment",
                50
            )

            result.setdefault(
                "recommendation",
                "Moderate Fit"
            )

            return result

    except Exception as e:

        print(
            f"Evaluation Agent Error: {e}"
        )

    return {
        "fit_score": 50,
        "technical_fit": 50,
        "ai_ml_alignment": 50,
        "career_alignment": 50,
        "recommendation": "Moderate Fit"
    }