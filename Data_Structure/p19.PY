# AB = [2, 1]
# CD = [4, 3]
# EF = [3, 2]
# GH = [6, 7]
 
# def Overlap(AB , CD, EF, GH):
#     x = 0
#     y = 1
#     x_dist = (min(CD[x], GH[x]) - max(AB[x], EF[x]))
#     y_dist = (min(CD[y], GH[y]) - max(AB[y], EF[y]))

#     area = 0
#     if x_dist > 0 and y_dist > 0:
#         area = x_dist * y_dist
 
#     return(area)
 
# print("Overlapping Area = {} squared units".format(Overlap(AB, CD, EF, GH)))
 


AB_CD = [[4, 3], [2, 1]]
AB_CD.sort()
# print(AB_CD)
# AB_CD = [[2, 1], [4, 3]]

EF_GH = [[6, 7], [3, 2]]
EF_GH.sort()
# print(EF_GH)
# EF_GH = [[3, 2], [6, 7]]

x = 0
y = 1
if EF_GH[0][x] in range(AB_CD[0][x], AB_CD[1][x]) and EF_GH[1][x] in range(AB_CD[0][x], AB_CD[1][x]):
    length = EF_GH[1][x] - EF_GH[0][x]
    print("both")
elif EF_GH[0][x] in range(AB_CD[0][x], AB_CD[1][x]):
    length = AB_CD[1][x] - EF_GH[0][x]
    print("left")
elif EF_GH[1][x] in range(AB_CD[0][x], AB_CD[1][x]):
    length = EF_GH[1][x] - AB_CD[0][x]
    print("right")
else:
    length = 0
    print('last')
print(length)
