from gemini import *
from prompt import *
from text_extractor import *
from generate_cv import *

text=model(prompt)
print(text)

# Extract summary and skills
cv_summary, cv_skills = extract_summary_and_skills(text)
generate_cv_template(name, cv_summary, cv_skills)
