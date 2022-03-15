import math
n = int(input("Enter a number to check if it is prime: "))

for i in range(2, math.floor(math.sqrt(n)) + 1):
    if n % i == 0:
        print("{} is NOT PRIME".format(n))
        break
else:
    print("{} is PRIME".format(n))

# -------------------OR---------------------------

# n = int(input("Enter a number to check if it is prime: "))

# finding the square root of input number
# if number is not perfect square, then find the nearest square root

# for i in range(1, int(n/2) + 1):
    
