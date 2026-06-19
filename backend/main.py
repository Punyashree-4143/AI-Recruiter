from src.ingestion import load_and_prepare_data


def main():

    documents, metadata = load_and_prepare_data(
        "../data/sample_candidates.json"
    )

    print(
        f"Successfully loaded "
        f"{len(documents)} candidates"
    )

    print("\nFIRST DOCUMENT:\n")

    print(documents[0][:1000])


if __name__ == "__main__":
    main()