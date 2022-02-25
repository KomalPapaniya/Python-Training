List = [1,0,2,2,0,1,0,1,2,0,0]
zero = []
one = []
two = []
for i in List:
    if i == 0:
        zero.append(i)
    elif i == 1:
        one.append(i)
    else:
        two.append(i)
print(zero + one + two)