# n = 999901

# if n % 9 == 0:
#     print(n%9+9)
# else:
#     print(n%9)

def house_of_rob(lst):
    a = 0
    b = 0
    for val in lst:
        a,b = b, max(b, val + a )
    return b

print(house_of_rob([2,11,7,2,6]))

