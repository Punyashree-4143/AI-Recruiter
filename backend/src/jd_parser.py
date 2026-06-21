import re


AI_SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "llm",
    "fine-tuning",
    "aws",
    "gcp",
    "mlops",
    "langchain",
    "rag",
    "pytorch",
    "tensorflow"
]


def parse_job_description(job_description):

    text = job_description.lower()

    detected_skills = []

    for skill in AI_SKILLS:

        if skill in text:
            detected_skills.append(skill)

    experience = 0

    exp_match = re.search(
        r'(\d+)\+?\s*years',
        text
    )

    if exp_match:
        experience = int(
            exp_match.group(1)
        )

    return {
        "required_skills":
            detected_skills,

        "minimum_experience":
            experience
    }