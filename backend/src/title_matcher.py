import re
from difflib import SequenceMatcher
from typing import Any


def normalize_title(title: str) -> str:
    normalized = re.sub(
        r"[^a-z0-9+#.]+",
        " ",
        (title or "").casefold(),
    )
    return " ".join(normalized.split())


def _title_similarity(left: str, right: str) -> float:
    normalized_left = normalize_title(left)
    normalized_right = normalize_title(right)

    if not normalized_left or not normalized_right:
        return 0.0

    if normalized_left == normalized_right:
        return 1.0

    left_tokens = set(normalized_left.split())
    right_tokens = set(normalized_right.split())

    if right_tokens and right_tokens.issubset(left_tokens):
        return 0.95

    token_score = (
        len(left_tokens & right_tokens)
        / len(left_tokens | right_tokens)
        if left_tokens and right_tokens
        else 0.0
    )
    sequence_score = SequenceMatcher(
        None,
        normalized_left,
        normalized_right,
    ).ratio()

    if not left_tokens & right_tokens:
        return 0.0

    return (
        token_score * 0.75
        + sequence_score * 0.25
    )


def calculate_title_match(
    title: str,
    role_profile: dict[str, Any],
) -> float:
    equivalent_titles = [
        role_profile.get("role", ""),
        *role_profile.get("equivalent_titles", []),
    ]
    related_titles = role_profile.get("related_titles", [])

    equivalent_score = max(
        (
            _title_similarity(title, target_title)
            for target_title in equivalent_titles
            if isinstance(target_title, str) and target_title.strip()
        ),
        default=0.0,
    )
    related_score = max(
        (
            _title_similarity(title, target_title)
            for target_title in related_titles
            if isinstance(target_title, str) and target_title.strip()
        ),
        default=0.0,
    )

    return max(equivalent_score, related_score * 0.7)
