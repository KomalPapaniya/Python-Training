import re

string = 'komal#papaniya%$python123%46'
g = re.sub(r'[^a-zA-Z0-9]', " ", string)
print(g)