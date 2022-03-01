A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
for i in set(A):
    if A.count(i) > len(A)/2:
        print(i)