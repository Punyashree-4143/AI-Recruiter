import re
from typing import Any


TOKEN_PATTERN = re.compile(
    r"c\+\+|c#|\.net|node\.js|ci/cd|[a-z0-9][a-z0-9.+#/-]*",
    re.IGNORECASE,
)


def normalize_text(value: str) -> str:
    return " ".join(
        token.casefold()
        for token in TOKEN_PATTERN.findall(value or "")
    )


def _contains_skill(document: str, skill: str) -> bool:
    normalized_document = f" {normalize_text(document)} "
    normalized_skill = normalize_text(skill)

    if not normalized_skill:
        return False

    return f" {normalized_skill} " in normalized_document


def calculate_skill_match(
    document: str,
    role_profile: dict[str, Any],
) -> dict[str, Any]:
    required_skills = list(
        dict.fromkeys(
            skill
            for skill in role_profile.get("required_skills", [])
            if isinstance(skill, str) and skill.strip()
        )
    )
    preferred_skills = list(
        dict.fromkeys(
            skill
            for skill in role_profile.get("preferred_skills", [])
            if isinstance(skill, str) and skill.strip()
        )
    )

    matched_required = [
        skill
        for skill in required_skills
        if _contains_skill(document, skill)
    ]
    missing_required = [
        skill
        for skill in required_skills
        if skill not in matched_required
    ]
    matched_preferred = [
        skill
        for skill in preferred_skills
        if _contains_skill(document, skill)
    ]

    required_coverage = (
        len(matched_required) / len(required_skills)
        if required_skills
        else 0.0
    )
    preferred_coverage = (
        len(matched_preferred) / len(preferred_skills)
        if preferred_skills
        else 0.0
    )

    return {
        "required_skill_coverage": required_coverage,
        "preferred_skill_coverage": preferred_coverage,
        "matched_required_skills": matched_required,
        "missing_required_skills": missing_required,
        "matched_preferred_skills": matched_preferred,
    }
