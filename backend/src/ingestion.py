import json


def load_and_prepare_data(file_path):
    """
    Load candidate data and prepare:

    1. documents -> text for embeddings
    2. metadata -> structured filtering data
    """

    documents = []
    metadata = []

    with open(file_path, "r", encoding="utf-8") as f:
        candidates = json.load(f)

    for candidate in candidates:

        profile = candidate.get("profile", {})
        career_history = candidate.get("career_history", [])
        education = candidate.get("education", [])
        skills = candidate.get("skills", [])
        certifications = candidate.get("certifications", [])
        languages = candidate.get("languages", [])
        signals = candidate.get("redrob_signals", {})

        # Skills
        skill_names = [
            skill.get("name", "")
            for skill in skills
        ]

        # Career History
        career_text = []

        for job in career_history:
            career_text.append(
                f"{job.get('title', '')} at "
                f"{job.get('company', '')}. "
                f"{job.get('description', '')}"
            )

        career_text = " ".join(career_text)

        # Education
        education_text = []

        for edu in education:
            education_text.append(
                f"{edu.get('degree', '')} in "
                f"{edu.get('field_of_study', '')} "
                f"from {edu.get('institution', '')}"
            )

        education_text = " ".join(education_text)

        # Certifications
        certification_text = ", ".join(
            cert.get("name", "")
            for cert in certifications
        )

        # Languages
        language_text = ", ".join(
            lang.get("language", "")
            for lang in languages
        )

        # Assessment Scores
        assessment_scores = signals.get(
            "skill_assessment_scores", {}
        )

        assessment_text = ", ".join(
            [
                f"{skill}:{score}"
                for skill, score
                in assessment_scores.items()
            ]
        )

        # Rich document for embeddings
        document = f"""
Candidate Name:
{profile.get('anonymized_name', '')}

Headline:
{profile.get('headline', '')}

Professional Summary:
{profile.get('summary', '')}

Current Title:
{profile.get('current_title', '')}

Current Industry:
{profile.get('current_industry', '')}

Years of Experience:
{profile.get('years_of_experience', 0)}

Skills:
{', '.join(skill_names)}

Career History:
{career_text}

Education:
{education_text}

Certifications:
{certification_text}

Languages:
{language_text}

Skill Assessment Scores:
{assessment_text}

GitHub Activity Score:
{signals.get('github_activity_score', -1)}

Recruiter Response Rate:
{signals.get('recruiter_response_rate', 0)}

Interview Completion Rate:
{signals.get('interview_completion_rate', 0)}

Saved By Recruiters:
{signals.get('saved_by_recruiters_30d', 0)}

Profile Completeness:
{signals.get('profile_completeness_score', 0)}

Open To Work:
{signals.get('open_to_work_flag', False)}
"""

        documents.append(document)

        metadata.append(
            {
                "candidate_id":
                    candidate.get("candidate_id"),

                "name":
                    profile.get("anonymized_name"),

                "location":
                    profile.get("location"),

                "country":
                    profile.get("country"),

                "current_title":
                    profile.get("current_title"),

                "industry":
                    profile.get("current_industry"),

                "years_of_experience":
                    profile.get("years_of_experience"),

                "open_to_work":
                    signals.get(
                        "open_to_work_flag"
                    ),

                "github_activity_score":
                    signals.get(
                        "github_activity_score"
                    ),

                "recruiter_response_rate":
                    signals.get(
                        "recruiter_response_rate"
                    ),

                "interview_completion_rate":
                    signals.get(
                        "interview_completion_rate"
                    ),

                "saved_by_recruiters_30d":
                    signals.get(
                        "saved_by_recruiters_30d"
                    ),

                "notice_period_days":
                    signals.get(
                        "notice_period_days"
                    ),

                "preferred_work_mode":
                    signals.get(
                        "preferred_work_mode"
                    ),

                "willing_to_relocate":
                    signals.get(
                        "willing_to_relocate"
                    )
            }
        )

    return documents, metadata