import re

string = 'area not a _a2_ roar took 22'
for i in string.split(" "):
    if i[-1] != 'a' and i[-1] != 'r':
        print(i, end = " ")
    else:
        print(re.sub(r' ', "\n", i))
