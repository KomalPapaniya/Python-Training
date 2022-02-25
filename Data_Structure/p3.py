List = [(2, 5, 8), (1, 2), (4, 4, 9, 6), (3, 3), (2, 1)]

List.sort(key = lambda a: a[len(a) - 1])
print(List)