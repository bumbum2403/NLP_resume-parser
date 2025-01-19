import re

def extract_mobile_number(resume_text):
    # Regular expression pattern to capture phone numbers
    phone_regex = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
    phone_numbers = re.findall(phone_regex, resume_text)
    
    # Return the first phone number found (assuming resumes typically have one primary number)
    if phone_numbers:
        return phone_numbers[0]
    else:
        return None

# Load textinput.txt and extract phone number
with open('/content/drive/My Drive/resume parser/textinput.txt', 'r') as file:
    textinput = file.read()

# Extract and print the phone number
mobile_number = extract_mobile_number(textinput)
if mobile_number:
    print('Mobile Number:', mobile_number)
else:
    print('No mobile number found in the resume.')

