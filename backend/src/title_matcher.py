AI_TITLES = [
    "ai engineer",
    "ml engineer",
    "machine learning engineer",
    "data scientist",
    "nlp engineer",
    "llm engineer",
    "recommendation systems engineer",
    "software engineer",
    "backend engineer",
    "cloud engineer",
    "devops engineer"
]


def calculate_title_match(title):

    title = title.lower()

    for ai_title in AI_TITLES:

        if ai_title in title:
            return 1

    return 0