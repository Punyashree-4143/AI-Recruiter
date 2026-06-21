export default function ComparisonPanel({
  comparison,
}) {
  const ranking = comparison?.ranking || [];

  return (
    <section className="card comparison-card">
      <div className="section-heading">
        <div>
          <p className="eyebrow">
            Candidate comparison
          </p>
          <h2>Shortlist perspective</h2>
        </div>
      </div>

      {ranking.length ? (
        <div className="comparison-list">
          {ranking.map((item, index) => (
            <article
              className="comparison-item"
              key={`${item.candidate_id}-${index}`}
            >
              <span className="position">
                {item.position || index + 1}
              </span>
              <div>
                <strong>{item.candidate_id}</strong>
                <p>
                  {item.reason
                    || "No comparison reason returned."}
                </p>
              </div>
            </article>
          ))}
        </div>
      ) : (
        <p className="empty-state">
          The comparison agent did not return a
          separate ranking.
        </p>
      )}
    </section>
  );
}
