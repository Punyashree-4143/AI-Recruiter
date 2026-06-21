from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def compare_candidates(
    job_description,
    candidates
):

    candidate_summaries = []

    for idx, candidate in enumerate(
        candidates,
        start=1
    ):

        candidate_summaries.append(
            f"""
Candidate {idx}

Candidate ID:
{candidate['candidate_id']}

Current Title:
{candidate['metadata'].get('current_title', '')}

Years of Experience:
{candidate['metadata'].get('years_of_experience', 0)}

Score:
{candidate['score']}

Recommendation:
{candidate.get('recommendation', '')}
"""
        )

    prompt = f"""
You are a senior recruiter.

Compare these shortlisted candidates for the role.

JOB DESCRIPTION:

{job_description}

CANDIDATES:

{''.join(candidate_summaries)}

Return ONLY valid JSON.

Format:

{{
    "ranking": [
        {{
            "candidate_id": "",
            "position": 1,
            "reason": ""
        }}
    ]
}}
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

            return json.loads(
                match.group()
            )

    except Exception as e:

        print(
            f"Comparison Agent Error: {e}"
        )

    return {
        "ranking": []
    }