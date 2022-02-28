string = "hello, komal papaniya here...!"
for i in string:
    if ord(i) - 32 in range(65, 91):
        print(chr(ord(i)-32), end = "")
    else:
        print(i, end = "")