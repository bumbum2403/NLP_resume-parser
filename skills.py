import re

def extract_skills(resume_text):
    skills = []
    
    # Define a list of skills to search for
    predefined_skills = [
        'Python', 'R', 'Java', 'TensorFlow', 'PyTorch', 'scikit-learn',
        'Keras', 'Pandas', 'NumPy', 'Matplotlib', 'AWS', 'Azure', 'Google Cloud'
    ]
    
    # Search for predefined skills in the resume text
    for skill in predefined_skills:
        if re.search(r'\b{}\b'.format(skill), resume_text, re.IGNORECASE):
            skills.append(skill)
    
    return skills

# Read textinput.txt for resume text
with open('/content/drive/My Drive/resume parser/textinput.txt', 'r') as file:
    textinput = file.read()

print('Skills: ', extract_skills(textinput))
