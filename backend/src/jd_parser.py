import re
from typing import Any


EXPERIENCE_PATTERNS = (
    re.compile(
        r"(\d+(?:\.\d+)?)\s*(?:\+|plus)?\s*years?"
        r"(?:\s+of)?\s+(?:relevant\s+)?experience",
        re.IGNORECASE,
    ),
    re.compile(
        r"minimum\s+(?:of\s+)?(\d+(?:\.\d+)?)\s*years?",
        re.IGNORECASE,
    ),
)

ROLE_PATTERNS = (
    re.compile(
        r"(?:hiring|seeking|looking for)\s+(?:an?\s+)?"
        r"([a-z][a-z0-9 /&+.-]{2,60}?)(?:[.,\n]|$)",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?:job title|position|role)\s*:\s*"
        r"([a-z][a-z0-9 /&+.-]{2,60}?)(?:[.,\n]|$)",
        re.IGNORECASE,
    ),
)

REQUIRED_HEADINGS = {
    "requirements",
    "required",
    "required skills",
    "must have",
    "must-have",
    "minimum qualifications",
    "qualifications",
}

PREFERRED_HEADINGS = {
    "preferred",
    "preferred skills",
    "nice to have",
    "nice-to-have",
    "desired",
    "bonus",
    "preferred qualifications",
}

STOP_HEADINGS = {
    "responsibilities",
    "about",
    "about us",
    "benefits",
    "education",
    "location",
    "what you will do",
    "what you'll do",
}


def _clean_heading(line: str) -> str:
    return re.sub(r"[:\s]+$", "", line.strip().casefold())


def _clean_list_item(line: str) -> str:
    value = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s*", "", line).strip()
    return value.rstrip(".,;")


def _is_list_item(line: str) -> bool:
    return bool(
        re.match(r"^\s*(?:[-*•]|\d+[.)])\s+\S", line)
    )


def _deduplicate(values: list[str]) -> list[str]:
    unique = []
    seen = set()

    for value in values:
        normalized = value.casefold().strip()
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique.append(value.strip())

    return unique


def _extract_section_items(job_description: str) -> tuple[list[str], list[str]]:
    required_skills = []
    preferred_skills = []
    active_section = None

    for raw_line in job_description.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        heading = _clean_heading(line)

        if heading in REQUIRED_HEADINGS:
            active_section = "required"
            continue

        if heading in PREFERRED_HEADINGS:
            active_section = "preferred"
            continue

        if heading in STOP_HEADINGS:
            active_section = None
            continue

        is_compact_plain_item = (
            active_section
            and len(line.split()) <= 8
            and not any(
                pattern.search(line)
                for pattern in EXPERIENCE_PATTERNS
            )
        )

        if active_section and (
            _is_list_item(raw_line)
            or is_compact_plain_item
        ):
            item = _clean_list_item(raw_line)
            if item:
                target = (
                    required_skills
                    if active_section == "required"
                    else preferred_skills
                )
                target.append(item)

    return _deduplicate(required_skills), _deduplicate(preferred_skills)


def _extract_experience(job_description: str) -> float:
    for pattern in EXPERIENCE_PATTERNS:
        match = pattern.search(job_description)
        if match:
            return float(match.group(1))
    return 0


def _extract_role(job_description: str) -> str:
    for pattern in ROLE_PATTERNS:
        match = pattern.search(job_description)
        if match:
            return " ".join(match.group(1).split())
    return ""


def parse_job_description(job_description: str) -> dict[str, Any]:
    required_skills, preferred_skills = _extract_section_items(
        job_description
    )
    experience_required = _extract_experience(job_description)
    role = _extract_role(job_description)

    return {
        "role": role,
        "required_skills": required_skills,
        "preferred_skills": preferred_skills,
        "equivalent_titles": [],
        "related_titles": [],
        "experience_required": experience_required,
        "minimum_experience": experience_required,
    }
