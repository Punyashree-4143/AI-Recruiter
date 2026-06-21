from src.jd_intelligence_agent import (
    understand_job_description
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

result = understand_job_description(
    job_description
)

print(result)