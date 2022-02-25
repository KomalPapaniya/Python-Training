List = [11, 45, 8, 11, 23, 45, 23, 45, 89]
result = {}
for i in List:
    result[i] = List.count(i)
print(result)

# ----------------------------------------------------

List = [11, 45, 8, 11, 23, 45, 23, 45, 89]
result = {}
for i in List:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1
print(result)
