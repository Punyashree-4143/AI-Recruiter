import { Link } from "react-router-dom";

import PageHeader from "../components/PageHeader";
import SkillList from "../components/SkillList";

export default function HiringDecisionPage({
  result,
}) {
  const decision = result.decision || {};
  const recommended = result.candidates?.find(
    (candidate) => (
      candidate.candidate_id
      === decision.recommended_candidate
    ),
  );

  return (
    <div className="page">
      <PageHeader
        eyebrow="Hiring recommendation"
        title="Final hiring decision"
        description={`Decision support for ${result.jd_analysis?.role || "the selected role"}.`}
        actions={
          <Link
            className="secondary-button"
            to="/candidates"
          >
            Review shortlist
          </Link>
        }
      />

      <section className="decision-hero">
        <div>
          <p className="eyebrow">
            Recommended candidate
          </p>
          <h2>
            {decision.recommended_candidate
              || "No recommendation returned"}
          </h2>
          {recommended && (
            <p>
              {recommended.metadata?.current_title}
              {" · "}
              {recommended.score} fit score
            </p>
          )}
        </div>
        <div className="confidence-ring">
          <strong>
            {Number(decision.confidence || 0)}
            %
          </strong>
          <span>confidence</span>
        </div>
      </section>

      <section className="decision-grid">
        <article className="card">
          <p className="eyebrow">Advantages</p>
          <h2>Strengths</h2>
          <SkillList
            skills={decision.strengths}
            tone="positive"
            emptyText="No strengths returned"
          />
        </article>

        <article className="card">
          <p className="eyebrow">Considerations</p>
          <h2>Risks</h2>
          <SkillList
            skills={decision.risks}
            tone="negative"
            emptyText="No risks returned"
          />
        </article>
      </section>

      <section className="card final-decision">
        <p className="eyebrow">Decision</p>
        <h2>Hiring manager summary</h2>
        <p>
          {decision.final_decision
            || "The hiring decision agent did not return a final summary."}
        </p>
      </section>
    </div>
  );
}
