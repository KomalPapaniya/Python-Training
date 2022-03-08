import re

List = ["komal", "kshitij;", "Aksh", "Vishruti", "Prachi;", "Praveen"]

for i in List:
    if re.search(r';$', i):
        print(i)