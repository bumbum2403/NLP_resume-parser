import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

EDUCATION = [
    'BE', 'B.E.', 'B.E', 'BS', 'B.S',
    'ME', 'M.E', 'M.E.', 'M.B.A', 'MBA', 'MS', 'M.S',
    'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
    'SSLC', 'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
]

def extract_education(resume_text):
    edu = {}
    sentences = resume_text.split('\n')
    
    for sentence in sentences:
        for word in sentence.split():
            word = re.sub(r'[?|$|.|!|,]', r'', word)
            if word.upper() in EDUCATION and word not in STOPWORDS:
                edu[word] = sentence
                
    education = []
    for key in edu.keys():
        year = re.search(r'(((20|19)(\d{})))', edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education

# Read textinput.txt for resume text
with open('/content/drive/My Drive/resume parser/textinput.txt', 'r') as file:
    textinput = file.read()

print('Qualification: ', extract_education(textinput))
