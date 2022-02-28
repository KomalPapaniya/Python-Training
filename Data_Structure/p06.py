List = [3, 6, 9, 1, 12, 7, 21]
def Reverse_List(List):
    n = len(List) - 1
    for i in range(len(List)):
        if i < n:
            List[i], List[n] = List[n], List[i]
        else:
            break
        n -= 1
    return List
print(Reverse_List(List))