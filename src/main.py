from utils import load_text
from analyzer import analyze

def main():
    resume_path = "data/resume.txt"
    job_path = "data/job_description.txt"

    resume_skills = load_text(resume_path)
    job_skills = load_text(job_path)

    matched, missing, score = analyze(resume_skills, job_skills)

    print("\nRESUME ANALYSIS REPORT")
    print("-" * 30)
    print(f"Match Score: {score}%")

    print("\nMatched Skills:")
    for skill in matched:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in missing:
        print(f"- {skill}")

if __name__ == "__main__":
    main()
