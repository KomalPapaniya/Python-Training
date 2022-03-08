import re
d = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87', '{{{melon-7}}}', 'guava--21']

for i in d:
    if re.findall(r'^{{[a-z]+[-]\d+}}$', i):
        print(i)
    elif re.findall(r'^[a-z]+[-]\d+$', i):
        print(i)