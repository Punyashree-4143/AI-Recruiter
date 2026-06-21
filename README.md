# AI Recruiter - Intelligent Candidate Ranking System

## Overview

Recruiters often review hundreds of profiles and still miss strong candidates because traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching.

AI Recruiter is an agentic AI-powered recruitment system that understands job requirements, evaluates candidate profiles holistically, and ranks candidates the way an experienced recruiter would.

Instead of relying only on job titles or keyword filters, the system analyzes:

* Job descriptions
* Career history
* Technical skills
* Experience level
* Candidate activity signals
* Semantic relevance
* Skill gaps
* Role alignment

The result is a recruiter-ready shortlist with explainable rankings and hiring recommendations.

---

## Problem Statement

Traditional recruitment systems suffer from several limitations:

* Over-reliance on keyword matching
* Poor understanding of career history
* Inability to identify transferable skills
* Lack of explainability
* High recruiter workload

This project addresses these challenges using semantic search, hybrid retrieval, LLM-powered analysis, and recruiter-style ranking.

---

## Key Features

### JD Intelligence Agent

Analyzes job descriptions and extracts:

* Role
* Domain
* Seniority
* Required Skills
* Preferred Skills
* Equivalent Titles
* Related Titles
* Experience Requirements

---

### Hybrid Candidate Retrieval

Uses:

* Dense Semantic Search (Embeddings)
* Sparse Keyword Search
* Hybrid Ranking

to retrieve the most relevant candidates.

---

### Recruiter Ranking Agent

Ranks candidates using:

* Required Skill Coverage
* Preferred Skill Coverage
* Title Similarity
* Experience Alignment
* Hybrid Retrieval Score

instead of simple keyword matching.

---

### Skill Gap Analysis

Identifies:

* Matched Skills
* Missing Skills
* Coverage Percentage

for every candidate.

---

### Explainability Agent

Provides transparent reasoning for every recommendation.

Example:

* Why candidate ranked highly
* Matched technologies
* Experience relevance
* Missing requirements

---

### Evaluation Agent

Uses LLM-based candidate assessment to evaluate:

* Technical Fit
* Role Alignment
* Experience Alignment
* Overall Fit Score

---

### Candidate Comparison Agent

Compares top candidates and generates a recruiter-style ranking explanation.

---

### Hiring Decision Agent

Produces:

* Recommended Candidate
* Confidence Score
* Strengths
* Risks
* Final Hiring Recommendation

---

## System Architecture

Job Description
↓
JD Intelligence Agent
↓
Hybrid Retrieval Engine
↓
Recruiter Ranking Agent
↓
Skill Gap Analyzer
↓
Explainability Agent
↓
Evaluation Agent
↓
Candidate Comparison Agent
↓
Hiring Decision Agent
↓
Final Candidate Shortlist

---

## Tech Stack

### Backend

* Python
* FastAPI
* Sentence Transformers
* FAISS
* BM25
* Groq LLM
* Pandas

### Frontend

* React
* Vite
* Axios
* React Router

### AI Components

* Semantic Embeddings
* Hybrid Search
* Agentic Workflow
* LLM Evaluation
* Explainable AI

---

## Project Structure

```text
backend/
│
├── api.py
├── search_candidates.py
├── requirements.txt
│
├── src/
│   ├── ingestion.py
│   ├── jd_parser.py
│   ├── jd_intelligence_agent.py
│   ├── hybrid_search.py
│   ├── recruiter_ranker.py
│   ├── ranking.py
│   ├── skill_matcher.py
│   ├── title_matcher.py
│   ├── skill_gap_analyzer.py
│   ├── explainability_agent.py
│   ├── evaluation_agent.py
│   ├── comparison_agent.py
│   ├── hiring_decision_agent.py
│   └── submission_generator.py
│
└── outputs/
    └── ranked_candidates.csv

frontend/
│
├── src/
│   ├── pages/
│   ├── components/
│   ├── services/
│   ├── App.jsx
│   ├── main.jsx
│   └── styles.css
│
├── package.json
└── vite.config.js
```

---

## Setup Instructions

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn api:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## API Endpoint

### Search Candidates

```http
POST /search-candidates
```

Request:

```json
{
  "job_description": "We are hiring a Senior Backend Engineer..."
}
```

Response:

```json
{
  "jd_analysis": {},
  "candidates": [],
  "comparison": {},
  "decision": {}
}
```

---

## Example Use Cases

### Backend Engineer

Skills:

* Java
* Spring Boot
* Kafka
* AWS

---

### Frontend Engineer

Skills:

* React
* TypeScript
* Next.js

---

### DevOps Engineer

Skills:

* Docker
* Kubernetes
* Terraform
* AWS

---

### AI Engineer

Skills:

* Python
* NLP
* LLM Fine-Tuning
* RAG

---

## Output

The system generates:

```text
outputs/ranked_candidates.csv
```

containing:

* Candidate ID
* Rank
* Score
* Recruiter Reasoning

---

## Future Enhancements

* Multi-job comparison
* Resume parsing
* Candidate chat assistant
* Interview question generation
* Real-time recruiter analytics
* ATS integrations
* Advanced talent intelligence

---

## Authors

Punyashree

MCA Candidate
Bangalore Institute of Technology

---

## License

This project was developed for an AI Recruitment Challenge / Hackathon submission.
