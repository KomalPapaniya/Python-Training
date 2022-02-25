integers = [1,2,3,4,5,6,7,8,9]

evenNumbers = []
oddNumbers = []

for num in integers:
    check = lambda n: n%2
    if check(num) == 0:
        evenNumbers.append(num)
    else:
        oddNumbers.append(num)

print("Even numbers list: ", evenNumbers)
print("Odd number list: ", oddNumbers)