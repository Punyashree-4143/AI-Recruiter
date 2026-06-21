from typing import Any

from src.ranking import calculate_candidate_score


def rank_candidates(
    hybrid_results,
    metadata,
    documents,
    query,
    role_profile: dict[str, Any] | None = None,
):
    metadata_map = {
        item["candidate_id"]: item
        for item in metadata
    }
    document_map = {
        item["candidate_id"]: documents[index]
        for index, item in enumerate(metadata)
        if index < len(documents)
    }
    scoring_profile = role_profile or (
        query if isinstance(query, dict) else {}
    )

    ranked_candidates = []

    for candidate_id, hybrid_score in hybrid_results:
        candidate_metadata = metadata_map.get(candidate_id, {})
        candidate_document = document_map.get(candidate_id, "")

        score_details = calculate_candidate_score(
            candidate_metadata=candidate_metadata,
            hybrid_score=hybrid_score,
            document=candidate_document,
            query=scoring_profile,
        )

        ranked_candidates.append(
            {
                "candidate_id": candidate_id,
                "score": score_details["final_score"],
                "score_breakdown": score_details,
                "metadata": candidate_metadata,
                "document": candidate_document,
            }
        )

    ranked_candidates.sort(
        key=lambda candidate: candidate["score"],
        reverse=True,
    )

    return ranked_candidates
