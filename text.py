import docx2txt
from PyPDF2 import PdfReader

def doctotext(m):
    temp = docx2txt.process(m)
    resume_text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
    text = ' '.join(resume_text)
    return text

def pdftotext(m):
    pdfFileObj = open(m, 'rb')
    pdfReader = PdfReader(pdfFileObj)
    num_pages = len(pdfReader.pages)
    text = ''
    for page_num in range(num_pages):
        page = pdfReader.pages[page_num]
        text += page.extract_text()
    return text

FilePath = '/content/drive/My Drive/resume parser/AI.pdf'  # Ensure your resume file is in the same directory
if FilePath.endswith('.docx'):
    textinput = doctotext(FilePath)
elif FilePath.endswith('.pdf'):
    textinput = pdftotext(FilePath)
else:
    raise ValueError("File not supported")

# Save the extracted text to a file
with open('/content/drive/My Drive/resume parser/textinput.txt', 'w') as f:
    f.write(textinput)
