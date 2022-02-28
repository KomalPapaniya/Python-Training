List = [9, 15, 1, 7, 10, 6, 8, 4]
result = []
n = len(List)
result.append(List[n-1])
for i in range(n-2,-1,-1):
    if List[i] > result[0]:
        result.insert(0,List[i])
print(result)