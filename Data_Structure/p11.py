List = [7, 5, 2, 3, 12, 9, 15, 24]
min_odd = max(List)
max_even = min(List)
for i in List:
    if i % 2 == 0 and i > max_even:
        max_even = i
    if i % 2 != 0 and i < min_odd:
        min_odd = i
print(min_odd * max_even)