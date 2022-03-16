# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

List = [(2, 5, 8), (1, 2), (4, 4, 9, 6), (3, 3), (2, 1)]

List.sort(key = lambda a: a[len(a) - 1])
print(List)