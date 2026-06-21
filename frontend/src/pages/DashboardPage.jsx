import { useState } from "react";
import { useNavigate } from "react-router-dom";

import PageHeader from "../components/PageHeader";
import { searchCandidates } from "../services/api";

const exampleJobDescription = `We are hiring a Senior Backend Engineer.

Requirements:
Java
Spring Boot
Microservices
Kafka
REST APIs
AWS

Preferred:
Docker
Kubernetes

5+ years experience.`;

export default function DashboardPage({
  result,
  setResult,
}) {
  const navigate = useNavigate();
  const [jobDescription, setJobDescription] = (
    useState("")
  );
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");

    if (jobDescription.trim().length < 20) {
      setError(
        "Add a complete job description before analyzing.",
      );
      return;
    }

    try {
      setLoading(true);
      const data = await searchCandidates(
        jobDescription.trim(),
      );
      setResult(data);
      navigate("/jd-analysis");
    } catch (requestError) {
      setError(
        requestError.response?.data?.detail
        || "The recruitment pipeline could not complete. Check that the backend is running and try again.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="page">
      <PageHeader
        eyebrow="Recruitment workspace"
        title="Find the strongest candidates for any role."
        description="Paste a job description to run JD intelligence, hybrid retrieval, recruiter ranking, evaluation, comparison, and hiring recommendation."
      />

      <section className="hero-grid">
        <form
          className="card search-card"
          onSubmit={handleSubmit}
        >
          <div className="field-header">
            <div>
              <label htmlFor="job-description">
                Job description
              </label>
              <p>
                Include requirements, preferred skills,
                and expected experience.
              </p>
            </div>
            <button
              className="text-button"
              type="button"
              onClick={() => (
                setJobDescription(
                  exampleJobDescription,
                )
              )}
            >
              Use example
            </button>
          </div>

          <textarea
            id="job-description"
            value={jobDescription}
            onChange={(event) => (
              setJobDescription(event.target.value)
            )}
            placeholder="Paste the complete job description here..."
            rows="18"
          />

          {error && (
            <div className="alert error">{error}</div>
          )}

          <div className="form-footer">
            <span>
              {jobDescription.trim().length} characters
            </span>
            <button
              className="primary-button"
              disabled={loading}
              type="submit"
            >
              {loading
                ? "Running recruiter pipeline..."
                : "Analyze candidates"}
            </button>
          </div>
        </form>

        <aside className="insight-stack">
          <section className="card compact-card">
            <p className="eyebrow">Pipeline</p>
            <h2>One search, six decisions</h2>
            <ol className="pipeline-list">
              <li>Understand the role</li>
              <li>Retrieve relevant profiles</li>
              <li>Rank candidate fit</li>
              <li>Analyze skill gaps</li>
              <li>Explain the shortlist</li>
              <li>Recommend a hire</li>
            </ol>
          </section>

          {result && (
            <section className="card compact-card accent-card">
              <p className="eyebrow">Previous search</p>
              <h2>
                {result.jd_analysis?.role
                  || "Recruitment analysis"}
              </h2>
              <p>
                {result.candidates?.length || 0}
                {" "}shortlisted candidates are available.
              </p>
              <button
                className="secondary-button"
                type="button"
                onClick={() => navigate("/candidates")}
              >
                View results
              </button>
            </section>
          )}
        </aside>
      </section>
    </div>
  );
}
