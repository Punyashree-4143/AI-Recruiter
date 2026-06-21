import {
  Link,
  useParams,
} from "react-router-dom";

import PageHeader from "../components/PageHeader";
import ScoreBadge from "../components/ScoreBadge";
import SkillList from "../components/SkillList";

export default function CandidateDetailsPage({
  result,
}) {
  const { candidateId } = useParams();
  const candidate = result.candidates?.find(
    (item) => (
      String(item.candidate_id)
      === decodeURIComponent(candidateId)
    ),
  );

  if (!candidate) {
    return (
      <div className="page">
        <section className="card empty-state-card">
          <h1>Candidate not found</h1>
          <Link to="/candidates">
            Return to candidate ranking
          </Link>
        </section>
      </div>
    );
  }

  const metadata = candidate.metadata || {};
  const gap = candidate.skill_gap || {};
  const explanation = candidate.explanation || {};
  const evaluation = candidate.evaluation || {};

  return (
    <div className="page">
      <PageHeader
        eyebrow="Candidate explainability"
        title={candidate.candidate_id}
        description={
          metadata.current_title || "Candidate profile"
        }
        actions={
          <Link
            className="secondary-button"
            to="/candidates"
          >
            Back to ranking
          </Link>
        }
      />

      <section className="metric-grid">
        <article className="metric-card">
          <span>Final score</span>
          <ScoreBadge score={candidate.score} />
        </article>
        <article className="metric-card">
          <span>Experience</span>
          <strong>
            {metadata.years_of_experience || 0}
            {" "}years
          </strong>
        </article>
        <article className="metric-card">
          <span>Skill coverage</span>
          <strong>
            {candidate.skill_coverage || 0}%
          </strong>
        </article>
        <article className="metric-card">
          <span>Recommendation</span>
          <strong>
            {candidate.recommendation
              || "Not available"}
          </strong>
        </article>
      </section>

      <section className="details-grid">
        <article className="card">
          <p className="eyebrow">Evidence</p>
          <h2>Matched required skills</h2>
          <SkillList
            skills={gap.matched_required}
            tone="positive"
            emptyText="No required skills matched"
          />
        </article>

        <article className="card">
          <p className="eyebrow">Skill gaps</p>
          <h2>Missing required skills</h2>
          <SkillList
            skills={gap.missing_required}
            tone="negative"
            emptyText="No required skill gaps"
          />
        </article>

        <article className="card">
          <p className="eyebrow">Additional fit</p>
          <h2>Matched preferred skills</h2>
          <SkillList
            skills={gap.matched_preferred}
            tone="primary"
          />
        </article>

        <article className="card">
          <p className="eyebrow">Evaluation</p>
          <h2>Fit evidence</h2>
          <SkillList
            skills={evaluation.evidence}
          />
        </article>
      </section>

      <section className="card explanation-card">
        <p className="eyebrow">Explainability summary</p>
        <h2>Why this candidate ranked here</h2>
        <div className="strength-list">
          {(explanation.strengths || []).map(
            (strength) => (
              <div
                className="strength-item"
                key={strength}
              >
                <span>✓</span>
                <p>{strength}</p>
              </div>
            ),
          )}
        </div>
      </section>
    </div>
  );
}
