def analyze(resume_skills, job_skills):
    """
    Compares resume skills with job description skills
    and returns matched skills, missing skills, and match score.
    """
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set - resume_set

    match_score = round((len(matched_skills) / len(job_set)) * 100, 2)

    return matched_skills, missing_skills, match_score
