# Return product of minimum of odd and maximum of even from a given list.
#        Sample = [7, 5,  2, 3, 12, 9, 15, 24]
#        Output = 72          #  (24 max even * 3 min odd)

List = [7, 5,  2, 3, 12, 9, 15, 24, -1, -3]
even_count = 0
odd_count = 0
for index in range(len(List)):
    if List[index] % 2 == 0 and even_count == 0:
        max_even = List[index]
        even_count += 1
    elif List[index] % 2 == 0:
        if List[index] > max_even:
            max_even = List[index]

    else:
        if odd_count == 0:
            min_odd = List[index]
            odd_count += 1
        elif List[index] < min_odd:
            min_odd = List[index]
print(min_odd * max_even)

# -----------------------------------------------------------
        
# List = [7, 5, 2, 3, 12, 9, 15, 24]
# min_odd = max(List)
# max_even = min(List)
# for index in List:
#     if index % 2 == 0 and index > max_even:
#         max_even = index
#     if index % 2 != 0 and index < min_odd:
#         min_odd = index
# print(min_odd * max_even)