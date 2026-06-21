from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import chromadb


MODEL_NAME = "all-MiniLM-L6-v2"


def semantic_search(query, top_k=20):

    model = SentenceTransformer(MODEL_NAME)

    query_embedding = model.encode(query)

    client = chromadb.PersistentClient(
        path="../vector_db"
    )

    collection = client.get_collection(
        name="candidates"
    )

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results


def bm25_search(query, documents, top_k=20):

    tokenized_docs = [
        doc.lower().split()
        for doc in documents
    ]

    bm25 = BM25Okapi(tokenized_docs)

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    return ranked_indices