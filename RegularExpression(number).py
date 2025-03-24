import re

def extract_phone_numbers(text):
    
    pattern = r'\b(?:\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}\b'
    
   
    phone_numbers = re.findall(pattern, text)
    
    return phone_numbers


text = "Contact us at (123) 4567890 or 987-654-3210 for more information."
result = extract_phone_numbers(text)
print("Extracted phone numbers:", result)
