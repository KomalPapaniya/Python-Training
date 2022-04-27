import numpy as np

n = 7
arr = np.zeros([n,n])
# print(arr)
num = 1
level = 0
row = 0
col = 0
itr_rotate = itr_remain = n

for i in range(1, n**2 + 1):
    if itr_remain <= 0:
        if level == 1:
            level = 2
            row -= 1
            col -= 1
            itr_remain = itr_rotate

        elif level == 2:
            level = 3
            row += 1
            col -= 1
            itr_rotate -= 1
            itr_remain = itr_rotate

        elif level == 3:
            level = 0
            row += 1
            col += 1
            itr_remain = itr_rotate
        
        elif level == 0:
            level = 1
            row += 1
            col -= 1
            itr_rotate -= 1
            itr_remain = itr_rotate

    if level == 0:
        arr[row][col] = num
        col += 1
    
    elif level == 1:
        arr[row][col] = num
        row += 1

    elif level == 2:
        arr[row][col] = num
        row -= 1

    elif level == 3:
        arr[row][col] = num
        col -= 1

    num += 1
    itr_remain -= 1

print(arr)