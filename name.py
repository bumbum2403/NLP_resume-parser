import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    nlp_text = nlp(resume_text)
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('NAME', [pattern])
    matches = matcher(nlp_text)
    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text

# Read textinput.txt to get the resume text
with open('/content/drive/My Drive/resume parser/textinput.txt', 'r') as file:
    textinput = file.read()

# Example usage: Extract and print the name based on textinput
extracted_name = extract_name(textinput)
print('Name: ', extracted_name)
