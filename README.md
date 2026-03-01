# Resume Analyzer (Python CLI Project)
A command-line based Python tool that analyzes how well a resume matches a job description.
It compares skills, highlights missing keywords, and generates a match percentage to help
users understand gaps before applying for a role.

This project is designed as an intermediate-level Python application focusing on clean
project structure, modular code, and practical real-world problem solving.

## Features
- Compares resume and job description text files
- Extracts and matches relevant skills
- Calculates a match percentage
- Identifies missing skills from the job description
- Clean, modular CLI-based design

## How It Works
1. The resume and job description are read from `.txt` files
2. Skills are normalized (lowercased & cleaned)
3. Common skills are identified using set operations
4. A match score is calculated based on overlap
5. Results are displayed in a clear terminal report

## Project Structure
resume-analyzer/
- src/
  - main.py # Entry point
  - analyzer.py # Core comparison logic
  - utils.py # File handling utilities
- data/
  - resume.txt
  - job_description.txt
- README.md
- requirements.txt

## How to Run
1. Clone the repository with the link: https://github.com/AkshraThareja/resume-analyzer.git
2. Open the folder in VS Code
3. Ensure Python 3 is installed
4. Run the following command in terminal:
python src/main.py

## Sample Output
RESUME ANALYSIS REPORT
------------------------------
Match Score: 66.67%

Matched Skills:
- python
- sql
- git
- communication

Missing Skills:
- apis
- data structures

## Future Improvements
1. Accept resume and job description file paths from user input
2. Support PDF resumes
3. Skill-weighted scoring (important vs optional skills)
4. Export analysis report to CSV or text file
5. Simple ATS-style keyboard ranking

## Concepts Practiced
1. File Handling
2. String processing
3. Set operations
4. Modular Python design
5. Git and GitHub workflow
