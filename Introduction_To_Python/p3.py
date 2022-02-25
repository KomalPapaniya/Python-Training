pair = list(map(int, input("Enter a pair of numbers: ").split()))
# print(pair)
divisors = []
for n in range(1, pair[0] + 1):
    if pair[0]%n == 0 and pair[1]%n == 0:
        divisors.append(n)
print(divisors)
