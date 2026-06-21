def generate_explanation(
    candidate,
    role_profile
):

    title = candidate["metadata"].get(
        "current_title",
        "Unknown"
    )

    experience = candidate["metadata"].get(
        "years_of_experience",
        0
    )

    coverage = candidate.get(
        "skill_coverage",
        0
    )

    matched = candidate[
        "skill_gap"
    ].get(
        "matched_required",
        []
    )

    missing = candidate[
        "skill_gap"
    ].get(
        "missing_required",
        []
    )

    strengths = []

    strengths.append(
        f"{experience} years experience"
    )

    strengths.append(
        f"{coverage}% required skill coverage"
    )

    strengths.append(
        f"Current role: {title}"
    )

    return {
        "title": title,
        "experience": experience,
        "coverage": coverage,
        "strengths": strengths,
        "matched_skills": matched,
        "missing_skills": missing
    }