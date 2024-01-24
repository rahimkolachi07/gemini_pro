from pdfminer.high_level import extract_text

def read_pdf():
    return extract_text("interview/Abdul Rahim (AI Engineer)     .pdf")
text=read_pdf()
print(text)