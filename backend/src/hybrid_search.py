from src.retrieval import semantic_search, bm25_search


def hybrid_search(query, documents, metadata, top_k=10):

    semantic_results = semantic_search(
        query,
        top_k=50
    )

    bm25_indices = bm25_search(
        query,
        documents,
        top_k=50
    )

    candidate_scores = {}

    # Semantic Results
    for rank, candidate_id in enumerate(
        semantic_results["ids"][0]
    ):

        semantic_score = (
            50 - rank
        ) / 50

        candidate_scores[candidate_id] = {
            "semantic_score":
                semantic_score,
            "bm25_score":
                0
        }

    # BM25 Results
    for rank, idx in enumerate(
        bm25_indices
    ):

        candidate_id = metadata[idx][
            "candidate_id"
        ]

        bm25_score = (
            50 - rank
        ) / 50

        if candidate_id not in candidate_scores:

            candidate_scores[
                candidate_id
            ] = {
                "semantic_score": 0,
                "bm25_score": bm25_score
            }

        else:

            candidate_scores[
                candidate_id
            ]["bm25_score"] = bm25_score

    final_results = []

    for candidate_id, scores in (
        candidate_scores.items()
    ):

        final_score = (
            scores["semantic_score"] * 0.7
            +
            scores["bm25_score"] * 0.3
        )

        final_results.append(
            (
                candidate_id,
                final_score
            )
        )

    final_results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return final_results[:top_k]