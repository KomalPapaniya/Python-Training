#  Return the sum of duplicates elements from the given List
# 			Ex. L = [3, 5, 6, 11, 12, 3, 5]
# 			Output = 8 (3+5)

List = [3, 5, 6, 11, 12, 3, 5, 5, 4, 4, 4]
duplicates = []
for element in List:
    if List.count(element) > 1 and element not in duplicates:
        duplicates.append(element)
        # print(duplicates)
 
tuple_str = ""  # to print the duplicates in tuple format...
for element in duplicates:  
    if duplicates.index(element) != len(duplicates) - 1:
        tuple_str += str(element) + "+"
tuple_str += str(duplicates[len(duplicates)-1])
 
print(sum(duplicates),"("+ tuple_str +")")