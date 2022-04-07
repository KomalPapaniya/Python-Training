num = int(input("Enter any number: "))

# while True:
#     sum = 0
#     for i in str(num):
#         sum += int(i)
#     num = sum
#     if len(str(num)) == 1:
#         break

# print(sum)

# -------------OR------------------------------

# sum = 0
# for i in str(num):
#     sum += int(i)
#     if sum > 9:
#         sum -= 9
# print(sum)

# -------------------OR-----------------------

if num % 9 == 0:
    print(num%9+9)
else:
    print(num%9)