import re

string = 'flag5 212jkl0, 212345 27, 212, 21209'
for i in string.split():
    if re.search(r'^212\d', i):
        print(i)
