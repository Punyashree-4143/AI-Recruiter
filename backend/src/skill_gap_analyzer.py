def analyze_skill_gap(
    document,
    required_skills,
    preferred_skills=None
):

    if preferred_skills is None:
        preferred_skills = []

    document_lower = document.lower()

    matched_required = []
    missing_required = []

    for skill in required_skills:

        if skill.lower() in document_lower:
            matched_required.append(skill)
        else:
            missing_required.append(skill)

    matched_preferred = []
    missing_preferred = []

    for skill in preferred_skills:

        if skill.lower() in document_lower:
            matched_preferred.append(skill)
        else:
            missing_preferred.append(skill)

    total_required = len(required_skills)

    coverage = 0

    if total_required > 0:

        coverage = round(
            (
                len(matched_required)
                / total_required
            ) * 100,
            2
        )

    return {
        "matched_required": matched_required,
        "missing_required": missing_required,
        "matched_preferred": matched_preferred,
        "missing_preferred": missing_preferred,
        "coverage": coverage
    }