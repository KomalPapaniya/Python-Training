String = "Komal Papaniya"
def Reverse(A):
    if len(A) == 0:
        return A
    else:
        # print(A)
        return Reverse(A[1:]) + A[0]
print(Reverse(String))
