L1 = []  # List 1
L2 = []  # List 2
# L1 = [1,2,3,6,7,9]
# L2 = [-1,0,4,5,6,9,10,11]

op_list = []  # output list
i1 = i2 = 0  # indices if List 1 and List 2
for i in range(len(L1) + len(L2)):
    if i1 >= len(L1):
        op_list.extend(L2[i2:])
        break
    elif i2 >= len(L2):
        op_list.extend(L1[i1:])
        break
    elif L1[i1] < L2[i2]:
        op_list.append(L1[i1])
        i1 += 1
    elif L1[i1] >= L2[i2]:
        op_list.append(L2[i2])
        i2 += 1

print(op_list)
