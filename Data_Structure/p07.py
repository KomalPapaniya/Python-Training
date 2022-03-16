# Convert any lower case string to upper case without in-built python functions.
# 			Ex. A = “abcdef ghi”
# 			Output: “ABCDEF GHI

string = "hello, komal papaniya here...!"
for char in string:
    if ord(char) - 32 in range(65, 91):
        print(chr(ord(char)-32), end = "")
    else:
        print(char, end = "")