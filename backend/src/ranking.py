from typing import Any

from src.skill_matcher import calculate_skill_match
from src.title_matcher import calculate_title_match


def _bounded_score(value: Any) -> float:
    try:
        return min(max(float(value), 0.0), 1.0)
    except (TypeError, ValueError):
        return 0.0


def _experience_score(
    years_of_experience: Any,
    experience_required: Any,
) -> float:
    try:
        years = max(float(years_of_experience or 0), 0)
        required = max(float(experience_required or 0), 0)
    except (TypeError, ValueError):
        return 0.0

    if required <= 0:
        return 0.0

    return min(years / required, 1.0)


def _experience_penalty(
    years_of_experience: Any,
    experience_required: Any,
) -> float:
    """
    Penalize candidates who do not meet
    minimum experience requirements.
    """

    try:
        years = max(float(years_of_experience or 0), 0)
        required = max(float(experience_required or 0), 0)
    except (TypeError, ValueError):
        return 1.0

    if required <= 0:
        return 1.0

    if years >= required:
        return 1.0

    gap = required - years

    penalty = max(
        0.50,
        1 - (gap * 0.10)
    )

    return penalty


def _weighted_average(
    components: list[tuple[float, float, bool]],
) -> float:

    active = [
        (score, weight)
        for score, weight, enabled in components
        if enabled
    ]

    total_weight = sum(
        weight
        for _, weight in active
    )

    if total_weight <= 0:
        return 0.0

    return sum(
        score * weight
        for score, weight in active
    ) / total_weight


def calculate_candidate_score(
    candidate_metadata: dict[str, Any],
    hybrid_score: float,
    document: str,
    query: Any,
) -> dict[str, Any]:

    role_profile = (
        query
        if isinstance(query, dict)
        else {
            "required_skills": [],
            "preferred_skills": [],
            "role": "",
            "equivalent_titles": [],
            "related_titles": [],
            "experience_required": 0,
        }
    )

    skill_match = calculate_skill_match(
        document,
        role_profile,
    )

    required_coverage = _bounded_score(
        skill_match["required_skill_coverage"]
    )

    preferred_coverage = _bounded_score(
        skill_match["preferred_skill_coverage"]
    )

    title_match = _bounded_score(
        calculate_title_match(
            candidate_metadata.get(
                "current_title",
                ""
            ),
            role_profile,
        )
    )

    experience_score = _experience_score(
        candidate_metadata.get(
            "years_of_experience",
            0
        ),
        role_profile.get(
            "experience_required",
            0
        ),
    )

    retrieval_score = _bounded_score(
        hybrid_score
    )

    has_required = bool(
        role_profile.get(
            "required_skills"
        )
    )

    has_preferred = bool(
        role_profile.get(
            "preferred_skills"
        )
    )

    has_titles = bool(
        role_profile.get("role")
        or role_profile.get(
            "equivalent_titles"
        )
        or role_profile.get(
            "related_titles"
        )
    )

    has_experience = bool(
        role_profile.get(
            "experience_required"
        )
    )

    final_score = _weighted_average(
        [
            (
                required_coverage,
                0.45,
                has_required
            ),
            (
                preferred_coverage,
                0.15,
                has_preferred
            ),
            (
                title_match,
                0.20,
                has_titles
            ),
            (
                experience_score,
                0.12,
                has_experience
            ),
            (
                retrieval_score,
                0.08,
                True
            ),
        ]
    )

    # ---------------------------------
    # Experience Penalty
    # ---------------------------------

    experience_penalty = _experience_penalty(
        candidate_metadata.get(
            "years_of_experience",
            0
        ),
        role_profile.get(
            "experience_required",
            0
        ),
    )

    final_score *= experience_penalty

    return {
        "final_score": round(
            final_score,
            4
        ),
        "skill_match": round(
            required_coverage,
            4
        ),
        "required_skill_coverage": round(
            required_coverage,
            4
        ),
        "preferred_skill_coverage": round(
            preferred_coverage,
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
        "experience_penalty": round(
            experience_penalty,
            4
        ),
        "retrieval_score": round(
            retrieval_score,
            4
        ),
        "matched_required_skills": skill_match[
            "matched_required_skills"
        ],
        "missing_required_skills": skill_match[
            "missing_required_skills"
        ],
        "matched_preferred_skills": skill_match[
            "matched_preferred_skills"
        ],
        "github_score": 0.0,
        "response_score": 0.0,
        "interview_score": 0.0,
        "open_to_work_score": 0.0,
    }