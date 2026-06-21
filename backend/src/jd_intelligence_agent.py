from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def understand_job_description(
    job_description
):

    prompt = f"""
You are a senior technical recruiter.

Analyze this job description.

JOB DESCRIPTION:

{job_description}

Return ONLY valid JSON.

Format:

{{
    "role": "",
    "domain": "",
    "required_skills": [],
    "preferred_skills": [],
    "target_titles": [],
    "search_query": ""
}}

Rules:

- Infer missing skills if obvious.
- Expand related AI skills.
- Include likely job titles.
- Create a semantic search query for vector search.

The search query should be a natural language phrase
containing:

- role names
- AI domains
- required skills
- preferred skills
- related technologies

Do NOT use:
AND
OR
NOT
Boolean operators

Return a single semantic search string.
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
            f"JD Agent Error: {e}"
        )

    return {
        "role": "",
        "domain": "",
        "required_skills": [],
        "preferred_skills": [],
        "target_titles": [],
        "search_query": job_description
    }