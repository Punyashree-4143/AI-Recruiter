export default function ScoreBadge({ score }) {
  const numericScore = Number(score) || 0;
  const tone = (
    numericScore >= 80
      ? "high"
      : numericScore >= 60
        ? "medium"
        : "low"
  );

  return (
    <span className={`score-badge ${tone}`}>
      {numericScore.toFixed(1)}
    </span>
  );
}
