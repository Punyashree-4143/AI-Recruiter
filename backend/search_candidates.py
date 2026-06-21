from src.ingestion import load_and_prepare_data
from src.jd_parser import parse_job_description
from src.jd_intelligence_agent import understand_job_description
from src.hybrid_search import hybrid_search
from src.recruiter_ranker import rank_candidates
from src.submission_generator import generate_submission
from src.evaluation_agent import evaluate_candidate
from src.comparison_agent import compare_candidates
from src.hiring_decision_agent import hiring_decision


def main():

    documents, metadata = load_and_prepare_data(
        "../data/candidates.jsonl"
    )

    job_description = """
    We are hiring an AI Engineer.

    Requirements:
    Python
    NLP
    LLM Fine-Tuning
    AWS

    Preferred:
    MLOps
    LangChain
    RAG

    3+ years experience.
    """

    # -----------------------------
    # JD Intelligence Agent
    # -----------------------------

    parsed_jd = parse_job_description(
        job_description
    )

    jd_analysis = understand_job_description(
        job_description
    )

    query = (
        " ".join(
            parsed_jd["required_skills"]
        )
        + " "
        + jd_analysis["search_query"]
    )

    print("\nJD Intelligence Agent Output:\n")
    print(jd_analysis)

    # -----------------------------
    # Retrieval Agent
    # -----------------------------

    hybrid_results = hybrid_search(
        query=query,
        documents=documents,
        metadata=metadata,
        top_k=50
    )

    # -----------------------------
    # Recruiter Ranking Agent
    # -----------------------------

    ranked_candidates = rank_candidates(
        hybrid_results=hybrid_results,
        metadata=metadata,
        documents=documents,
        query=query
    )

    # -----------------------------
    # Evaluation Agent
    # -----------------------------

    print(
        "\nRunning Recruiter Evaluation Agent...\n"
    )

    top_candidates = ranked_candidates[:20]

    for candidate in top_candidates:

        evaluation = evaluate_candidate(
            job_description,
            candidate
        )

        candidate["llm_fit_score"] = (
            evaluation.get(
                "fit_score",
                50
            )
        )

        candidate["recommendation"] = (
            evaluation.get(
                "recommendation",
                "Moderate Fit"
            )
        )

        llm_score = (
            evaluation.get(
                "fit_score",
                50
            ) * 0.5
            +
            evaluation.get(
                "technical_fit",
                50
            ) * 0.2
            +
            evaluation.get(
                "ai_ml_alignment",
                50
            ) * 0.2
            +
            evaluation.get(
                "career_alignment",
                50
            ) * 0.1
        )

        candidate["score"] = round(
            (
                candidate["score"] * 100 * 0.60
            )
            +
            (
                llm_score * 0.40
            ),
            2
        )

    top_candidates.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # -----------------------------
    # Comparison Agent
    # -----------------------------

    print(
        "\nRunning Candidate Comparison Agent...\n"
    )

    comparison_result = compare_candidates(
        job_description,
        top_candidates
    )

    print(
        "\nComparison Agent Output:\n"
    )

    print(
        comparison_result
    )

    # -----------------------------
    # Hiring Decision Agent
    # -----------------------------

    print(
        "\nRunning Hiring Decision Agent...\n"
    )

    decision = hiring_decision(
        job_description,
        comparison_result,
        top_candidates
    )

    print(
        "\nHiring Decision:\n"
    )

    print(
        decision
    )

    # -----------------------------
    # Save Results
    # -----------------------------

    ranked_candidates = top_candidates

    generate_submission(
        ranked_candidates=ranked_candidates,
        output_path="../outputs/ranked_candidates.csv",
        job_description=job_description
    )

    print(
        "\nSearch completed successfully."
    )


if __name__ == "__main__":
    main()