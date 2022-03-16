# Add 1 to given list elements. Do not use string conversion.
# 	Sample = [1, 2, 3]
#   Output = [1, 2, 4]

List = [3, 5, 9, 9]
n = len(List) - 1
num = 0
for element in List:
    num += element * 10**n
    n -= 1
num += 1
result = []
while num > 0:
    result.append(num % 10)
    num //= 10
result.reverse()
print(result)  