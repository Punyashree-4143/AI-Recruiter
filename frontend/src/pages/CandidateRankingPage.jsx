import { Link } from "react-router-dom";

import ComparisonPanel from "../components/ComparisonPanel";
import PageHeader from "../components/PageHeader";
import ScoreBadge from "../components/ScoreBadge";

export default function CandidateRankingPage({
  result,
}) {
  const candidates = result.candidates || [];

  return (
    <div className="page">
      <PageHeader
        eyebrow="Recruiter ranking"
        title="Ranked candidates"
        description={`Candidate fit for ${result.jd_analysis?.role || "the selected role"}, combining the existing retrieval, ranking, and evaluation pipeline.`}
        actions={
          <Link
            className="primary-button"
            to="/decision"
          >
            View hiring decision
          </Link>
        }
      />

      <section className="card table-card">
        <div className="table-scroll">
          <table>
            <thead>
              <tr>
                <th>Rank</th>
                <th>Candidate ID</th>
                <th>Current title</th>
                <th>Score</th>
                <th>Skill coverage</th>
                <th>Recommendation</th>
                <th aria-label="Candidate details" />
              </tr>
            </thead>
            <tbody>
              {candidates.map((candidate, index) => (
                <tr key={candidate.candidate_id}>
                  <td>
                    <span className="rank-number">
                      {index + 1}
                    </span>
                  </td>
                  <td>
                    <strong>
                      {candidate.candidate_id}
                    </strong>
                  </td>
                  <td>
                    {candidate.metadata?.current_title
                      || "Unknown"}
                  </td>
                  <td>
                    <ScoreBadge
                      score={candidate.score}
                    />
                  </td>
                  <td>
                    <div className="coverage-cell">
                      <div className="progress-track">
                        <span
                          style={{
                            width: `${Math.min(candidate.skill_coverage || 0, 100)}%`,
                          }}
                        />
                      </div>
                      <strong>
                        {candidate.skill_coverage || 0}%
                      </strong>
                    </div>
                  </td>
                  <td>
                    <span className="recommendation">
                      {candidate.recommendation
                        || "Not available"}
                    </span>
                  </td>
                  <td>
                    <Link
                      className="table-link"
                      to={`/candidates/${encodeURIComponent(candidate.candidate_id)}`}
                    >
                      Details
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      <ComparisonPanel
        comparison={result.comparison}
      />
    </div>
  );
}
