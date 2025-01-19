import re

def extract_email(resume_text):
    # Regular expression pattern to capture email addresses
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   
    emails = re.findall(email_regex, resume_text)

    # Return the first email found (assuming resumes typically have one primary email)
    if emails:
        return emails[0]
    else:
        return None

# Load textinput.txt and extract email address
with open('/content/drive/My Drive/resume parser/textinput.txt', 'r') as file:
    textinput = file.read()

# Extract and print the email address
email = extract_email(textinput)
if email:
    print('Email:', email)
else:
    print('No email address found in the resume.')
