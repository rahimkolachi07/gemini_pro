from gemini.gemini import *
from interview.pdf_word_file_reader import*
text=model("write scipts for introdcution of machine learning engineer for power point slids")
print(text)
def interview(pdf,job_title,job_description):
    cv=read_pdf(pdf)
    text_g="""Given a user's resuma = {cv},job_title= {job_title}, job_description={job_description}, and company={company} , the model should:

    1. Analyze the CV:
    - Identify the user's skills, experiences, and qualifications.
    - Compare these with the requirements and preferences listed in the job description.
    - Generate suggestions for improving the CV to better match the job description.

    2. Prepare for the interview:
    - Generate a list of potential interview questions based on the job description and company.
    - Provide guidance on how to answer these questions based on the user's background and the company's culture and values.
    - Offer tips for discussing the user's skills and experiences in a way that aligns with the company's needs and values.

    3. Provide guidance for the specific job:
    - Offer insights into the company's culture, values, and expectations.
    - Provide tips for succeeding in the role, such as skills to develop or industry trends to follow.

    The model should provide these outputs in a clear, concise, and actionable format, enabling the user to effectively prepare for their job interview and improve their chances of success.
    """

    text=model(text_g)
    print(text)
interview("interview/Abdul Rahim (AI Engineer)     .pdf","machine learning","developing and testing machine learning models","google")