import subprocess
from openai import OpenAI

client = OpenAI()

start_date = "2026-03-09"
end_date = "2026-05-22"

git_output = subprocess.check_output([
    "git",
    "log",
    f"--since={start_date}",
    f"--until={end_date}",
    "--patch",
    "--stat"
]).decode()

prompt = f"""
Generate a weekly engineering dossier from this git history.

Include:
- executive summary
- features
- bug fixes
- infra/devops
- refactors
- risks
- technical highlights
- WHY changes happened
- WHAT systems were affected
- WHAT future risks exist

Git data:
{git_output}
"""

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

report = response.choices[0].message.content

with open("content/Dossier.md", "w") as f:
    f.write(report)

print(report)