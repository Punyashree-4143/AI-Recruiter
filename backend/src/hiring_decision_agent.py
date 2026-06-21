from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def hiring_decision(
    job_description,
    comparison_result,
    candidates
):

    candidate_summary = []

    for candidate in candidates[:5]:

        candidate_summary.append(
            f"""
Candidate ID:
{candidate['candidate_id']}

Title:
{candidate['metadata'].get('current_title', '')}

Experience:
{candidate['metadata'].get('years_of_experience', 0)}

Score:
{candidate['score']}

Recommendation:
{candidate.get('recommendation', '')}
"""
        )

    prompt = f"""
You are a senior hiring manager.

JOB DESCRIPTION:

{job_description}

COMPARISON RESULT:

{comparison_result}

TOP CANDIDATES:

{''.join(candidate_summary)}

Select the best candidate.

Return ONLY valid JSON.

Format:

{{
    "recommended_candidate": "",
    "confidence": 0,
    "strengths": [],
    "risks": [],
    "final_decision": ""
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
            f"Hiring Decision Agent Error: {e}"
        )

    return {
        "recommended_candidate": "",
        "confidence": 0,
        "strengths": [],
        "risks": [],
        "final_decision": ""
    }