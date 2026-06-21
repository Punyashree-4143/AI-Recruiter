from src.ingestion import load_and_prepare_data
from src.embeddings import create_vector_store


def main():

    print("Loading candidates...")

    documents, metadata = load_and_prepare_data(
        "../data/candidates.jsonl"
    )

    print(
        f"Loaded {len(documents)} candidates"
    )

    create_vector_store(
        documents,
        metadata
    )

    print(
        "Indexing completed successfully."
    )


if __name__ == "__main__":
    main()