import re

email = 'abc_123@xyz.com'
p = re.findall(r'\w+@', email)
print(p)