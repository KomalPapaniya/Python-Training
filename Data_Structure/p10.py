# Find the max sum of sub array
# 			Ex L = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
# 			Output = 49

List = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
sum_array = []
for index_1 in range(len(List)):
    for index_2 in range(index_1 + 1, len(List)):
        sum_array.append(sum(List[index_1:index_2+1]))
print(max(sum_array))
