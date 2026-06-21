def generate_reasoning(
    candidate_metadata,
    score_breakdown
):
    title = candidate_metadata.get(
        "current_title",
        "Professional"
    )

    experience = candidate_metadata.get(
        "years_of_experience",
        0
    )

    response_rate = candidate_metadata.get(
        "recruiter_response_rate",
        0
    )

    reasoning = (
        f"{title} with "
        f"{experience} years experience; "
        f"skill match "
        f"{score_breakdown['skill_match']}; "
        f"response rate "
        f"{response_rate}"
    )

    return reasoning