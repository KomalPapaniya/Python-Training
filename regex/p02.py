import re

string = "decision, apple 12345678, property a 49583229 lifetime"
eight_letter_word = re.findall(r'\b[a-zA-Z]{8}\b', string)

print(eight_letter_word)