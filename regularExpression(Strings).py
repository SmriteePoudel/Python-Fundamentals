import re

def extract_five_letter_words(text):
    
    pattern = r'\b\w{5}\b'
    
   
    five_letter_words = re.findall(pattern, text)
    
    return five_letter_words


text = "There are words like apple, mango, and happy in this sentence."
result = extract_five_letter_words(text)
print("Words with exactly 5 characters:", result)
