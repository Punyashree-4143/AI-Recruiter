AI_SKILLS = {
    "python",
    "machine learning",
    "deep learning",
    "nlp",
    "llm",
    "fine-tuning llms",
    "lora",
    "aws",
    "gcp",
    "mlops",
    "tensorflow",
    "pytorch",
    "langchain",
    "rag",
    "vector databases",
    "computer vision"
}


def calculate_skill_match(
    document,
    query
):

    document = document.lower()
    query = query.lower()

    matched = 0
    total = 0

    for skill in AI_SKILLS:

        if skill in query:

            total += 1

            if skill in document:

                matched += 1

    if total == 0:
        return 0

    return matched / total