ab = [-3, 2]
cd = [1, -3]
ef = [3, -2]
gh = [-4, -7]

AB = []
CD = []
EF = []
GH = []

AB.append(min(ab[0], cd[0]))
AB.append(min(ab[1], cd[1]))
# print(AB)

CD.append(max(ab[0], cd[0]))
CD.append(max(ab[1], cd[1]))
# print(CD)

EF.append(min(ef[0], gh[0]))
EF.append(min(ef[1], gh[1]))
# print(EF)

GH.append(max(ef[0], gh[0]))
GH.append(max(ef[1], gh[1]))
# print(GH)
 
def Overlap(AB , CD, EF, GH):
    x = 0
    y = 1
    x_dist = (min(CD[x], GH[x]) - max(AB[x], EF[x]))
    y_dist = (min(CD[y], GH[y]) - max(AB[y], EF[y]))

    area = 0
    if x_dist > 0 and y_dist > 0:
        area = x_dist * y_dist
 
    return(area)
 
print("Overlapping Area = {} squared units".format(Overlap(AB, CD, EF, GH)))
 
