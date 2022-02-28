List = [3, 5, 6, 11, 12, 3, 5, 5, 4, 4, 4]
duplicates = []
for i in List:
    if List.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
 
s = ""  # to print the duplicates in tuple format...
for i in duplicates:  
    if duplicates.index(i) != len(duplicates) - 1:
        s += str(i)+"+"
s += str(duplicates[len(duplicates)-1])
 
print(sum(duplicates),"("+s+")")