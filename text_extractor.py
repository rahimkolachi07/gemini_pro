def extract_summary_and_skills(raw_data):
    # Split raw data into sections
    sections = raw_data.split("**")

    # List of possible headers for the summary
    summary_headers = ["Summary", "Summary:", "About Me"]

    # List of possible headers for skills
    skills_headers = ["Skills", "Skills:", "Expertise"]

    # Extract summary and skills
    summary = None
    skills = None

    for header in summary_headers:
        if header in sections:
            summary = sections[sections.index(header) + 1].strip()
            break

    for header in skills_headers:
        if header in sections:
            skills = sections[sections.index(header) + 1].strip()
            break

    return summary, skills
