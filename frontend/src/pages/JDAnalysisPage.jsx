import { Link } from "react-router-dom";

import PageHeader from "../components/PageHeader";
import SkillList from "../components/SkillList";

export default function JDAnalysisPage({ result }) {
  const analysis = result.jd_analysis || {};

  return (
    <div className="page">
      <PageHeader
        eyebrow="JD intelligence"
        title={analysis.role || "Role analysis"}
        description="The structured role profile used by retrieval, ranking, and evaluation."
        actions={
          <Link
            className="primary-button"
            to="/candidates"
          >
            View ranked candidates
          </Link>
        }
      />

      <section className="metric-grid">
        <article className="metric-card">
          <span>Role</span>
          <strong>{analysis.role || "Not specified"}</strong>
        </article>
        <article className="metric-card">
          <span>Domain</span>
          <strong>
            {analysis.domain || "Not specified"}
          </strong>
        </article>
        <article className="metric-card">
          <span>Experience required</span>
          <strong>
            {analysis.experience_required
              ? `${analysis.experience_required}+ years`
              : "Not specified"}
          </strong>
        </article>
        <article className="metric-card">
          <span>Shortlisted</span>
          <strong>
            {result.candidates?.length || 0}
            {" "}candidates
          </strong>
        </article>
      </section>

      <section className="analysis-grid">
        <article className="card">
          <p className="eyebrow">Must have</p>
          <h2>Required skills</h2>
          <SkillList
            skills={analysis.required_skills}
            tone="primary"
          />
        </article>

        <article className="card">
          <p className="eyebrow">Nice to have</p>
          <h2>Preferred skills</h2>
          <SkillList
            skills={analysis.preferred_skills}
            tone="positive"
          />
        </article>

        <article className="card">
          <p className="eyebrow">Equivalent</p>
          <h2>Equivalent titles</h2>
          <SkillList
            skills={
              analysis.equivalent_titles
              || analysis.target_titles
            }
          />
        </article>

        <article className="card">
          <p className="eyebrow">Adjacent talent</p>
          <h2>Related titles</h2>
          <SkillList
            skills={analysis.related_titles}
          />
        </article>
      </section>

      <section className="card query-card">
        <p className="eyebrow">Retrieval query</p>
        <h2>Semantic search context</h2>
        <p>
          {analysis.search_query
            || "No search query was returned."}
        </p>
      </section>
    </div>
  );
}
