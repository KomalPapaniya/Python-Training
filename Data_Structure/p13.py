# Return the array which contains the elements which are greater than from its right side
# 	Sample = [5, 17, 2, 6, 3]
# 	Output = [17, 6, 3] 

List = [9, 15, 1, 7, 10, 6, 8, 4]
result = []
last_index = len(List) - 1
result.append(List[last_index])
for index in range(last_index-1,-1,-1):
    if List[index] > result[0]:
        result.insert(0,List[index])
print(result)