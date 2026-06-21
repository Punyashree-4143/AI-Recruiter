import pandas as pd

from src.llm_ranker import (
    generate_llm_reasoning
)


def generate_submission(
    ranked_candidates,
    output_path,
    job_description
):

    rows = []

    for rank, candidate in enumerate(
        ranked_candidates,
        start=1
    ):

        try:

            reasoning = generate_llm_reasoning(
                job_description,
                candidate
            )

        except Exception as e:

            print(
                f"Groq Error: {e}"
            )

            reasoning = (
                "Reasoning generation failed."
            )

        rows.append(
            {
                "candidate_id":
                    candidate["candidate_id"],

                "rank":
                    rank,

                "score":
                    candidate["score"],

                "reasoning":
                    reasoning
            }
        )

    df = pd.DataFrame(rows)

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Submission saved to: {output_path}"
    )