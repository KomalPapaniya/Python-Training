a = int(input("a = "))
b = int(input("b = "))

while(b != 0):
    x = a & b
    a = a ^ b
    b = x << 1
print(a)