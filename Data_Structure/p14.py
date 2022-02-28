List = [3, 5, 9, 9]
n = len(List) - 1
num = 0
for i in List:
    num += i * 10**n
    n -= 1
num += 1
result = []
while num > 0:
    result.append(num % 10)
    num //= 10
result.reverse()
print(result)