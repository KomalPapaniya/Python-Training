import json

try:
    with open("student.json", 'r') as s:
        details = json.load(s)
        print(details)
except:
    print("Error")