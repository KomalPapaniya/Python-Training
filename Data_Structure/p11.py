List = [7, 5,  2, 3, 12, 9, 15, 24, -1, -3]
even_count = 0
odd_count = 0
for i in range(len(List)):
    if List[i] % 2 == 0 and even_count == 0:
        max_even = List[i]
        even_count += 1
    elif List[i] % 2 == 0:
        if List[i] > max_even:
            max_even = List[i]

    else:
        if odd_count == 0:
            min_odd = List[i]
            odd_count += 1
        elif List[i] < min_odd:
            min_odd = List[i]
print(min_odd * max_even)

# -----------------------------------------------------------
        
# List = [7, 5, 2, 3, 12, 9, 15, 24]
# min_odd = max(List)
# max_even = min(List)
# for i in List:
#     if i % 2 == 0 and i > max_even:
#         max_even = i
#     if i % 2 != 0 and i < min_odd:
#         min_odd = i
# print(min_odd * max_even)