from src.skill_matcher import calculate_skill_match
from src.title_matcher import calculate_title_match


def calculate_candidate_score(
    candidate_metadata,
    hybrid_score,
    document,
    query
):
    """
    Recruiter-style candidate scoring.
    """

    # Skill Match
    skill_match = calculate_skill_match(
        document,
        query
    )

    # Title Match
    title_match = calculate_title_match(
        candidate_metadata.get(
            "current_title",
            ""
        )
    )

    # Experience Score
    experience_score = min(
        candidate_metadata.get(
            "years_of_experience",
            0
        ) / 15,
        1
    )

    # GitHub Score
    github_score = max(
        candidate_metadata.get(
            "github_activity_score",
            0
        ),
        0
    ) / 100

    # Recruiter Response Rate
    response_score = (
        candidate_metadata.get(
            "recruiter_response_rate",
            0
        )
    )

    # Interview Completion Rate
    interview_score = (
        candidate_metadata.get(
            "interview_completion_rate",
            0
        )
    )

    # Open To Work
    open_to_work_score = (
        1
        if candidate_metadata.get(
            "open_to_work",
            False
        )
        else 0
    )

    # Final Recruiter Score
    final_score = (
        skill_match * 0.30 +
        title_match * 0.20 +
        hybrid_score * 0.20 +
        experience_score * 0.10 +
        github_score * 0.10 +
        response_score * 0.05 +
        interview_score * 0.03 +
        open_to_work_score * 0.02
    )

    return {
        "final_score": round(
            final_score,
            4
        ),
        "skill_match": round(
            skill_match,
            4
        ),
        "title_match": round(
            title_match,
            4
        ),
        "experience_score": round(
            experience_score,
            4
        ),
        "github_score": round(
            github_score,
            4
        ),
        "response_score": round(
            response_score,
            4
        ),
        "interview_score": round(
            interview_score,
            4
        ),
        "open_to_work_score": round(
            open_to_work_score,
            4
        )
    }