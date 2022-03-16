# Create a function to reverse the entire list without any function and also do not use any indexing or slicing shortcut. Time Complexity O(logn)

List = [3, 6, 9, 1, 12, 7, 21]
def Reverse_List(List):
    end = len(List) - 1
    for start in range(len(List)):
        if start < end:
            List[start], List[end] = List[end], List[start]
        else:
            break
        end -= 1
    return List
print(Reverse_List(List))