import re

string = 'y7u0 l8 1f9'
digits = re.findall(r'\d', string)
print(digits)