export default function SkillList({
  skills = [],
  tone = "neutral",
  emptyText = "None specified",
}) {
  if (!skills.length) {
    return (
      <span className="empty-text">{emptyText}</span>
    );
  }

  return (
    <div className="skill-list">
      {skills.map((skill) => (
        <span
          className={`skill-tag ${tone}`}
          key={skill}
        >
          {skill}
        </span>
      ))}
    </div>
  );
}
