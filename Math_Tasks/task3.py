# Find area between 2 overlapping polygons (can be any type of polygon)
# polygon1 = [(-10, 30), (10, 20), (15, 10), (-20, 10)]
# polygon2 = [(-20, 25), (15, 25), (15, 15), (-20, 20)]
# Area = 172

P1 = [(-10, 30), (10, 20), (15, 10), (-20, 10)]

P2 = [(-20, 25), (15, 25), (15, 15), (-20, 20)]

INT_MAX = 10000
INT_MIN = -10000
points = []

# class Point:
#     def __init__(self, tup):
#         self.x = tup[0]
#         self.y = tup[1]
        
def onSegment(p, q, r):
    if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and
           (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    return False
 
def orientation(p, q, r):
     
    val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
    if (val > 0):
         
        # Clockwise orientation
        return 1
    elif (val < 0):
         
        # Counterclockwise orientation
        return 2
    else:
         
        # Collinear orientation
        return 0

def doIntersect(p1,q1,p2,q2):

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return 1
 
    # Special Cases
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return 5
 
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return 5
 
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return 5

    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return 5

    return False

def intPoint(p1,q1,p2,q2):
    xdiff = (p1[0] - q1[0], p2[0] - q2[0])
    ydiff = (p1[1] - q1[1], p2[1] - q2[1])
    
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')
    
    d = (det((p1[0], p1[1]),(q1[0], q1[1])), det((p2[0], p2[1]),(q2[0], q2[1])))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def rIntersection(points, p):
     
    n = len(points)
         
    extreme = (INT_MAX, p[1])
    count = i = 0
     
    while True:
        next = (i + 1) % n

        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):

            if orientation(points[i], p,
                           points[next]) == 0:
                return onSegment(points[i], p,
                                 points[next])              
            count += 1
            
        i = next
        if (i == 0):
            break
         
    return (count)

 
def lIntersection(points, p):
     
    n = len(points)

    extreme = (INT_MIN, p[1])
    count = i = 0
     
    while True:
        next = (i + 1) % n

        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):

            if orientation(points[i], p,
                           points[next]) == 0:
                return onSegment(points[i], p,
                                 points[next])
                                  
            count += 1
#             print('count= ', count)
             
        i = next
         
        if (i == 0):
            break

    return (count)

for i in range(len(P1)):
    for j in range(len(P2)):
        flag = 0
        if i != len(P1) - 1 and j != len(P2) - 1:
            p1 = P1[i]
            q1 = P1[i+1]
            p2 = P2[j]
            q2 = P2[j+1]

            if doIntersect(p1, q1, p2, q2):
#                 print("Yes")
                flag = 1
#                 print(P1[i], P1[i+1])
#                 print(P2[j], P2[j+1])
            
        if i != len(P1) - 1 and j == len(P2) - 1:
            p1 = P1[i]
            q1 = P1[i+1]
            p2 = P2[j]
            q2 = P2[0]
            
            if doIntersect(p1, q1, p2, q2):
#                 print("Yes")
                flag = 1
#                 print(P1[i], P1[i+1])
#                 print(P2[j], P2[0])
                
        if i == len(P1) - 1 and j != len(P2) - 1:
            p1 = P1[i]
            q1 = P1[0]
            p2 = P2[j]
            q2 = P2[j+1]
            
            if doIntersect(p1, q1, p2, q2):
#                 print("Yes")
                flag = 1
#                 print(P1[i], P1[0])
#                 print(P2[j], P2[j+1])
                
        if i == len(P1) - 1 and j == len(P2) - 1:
            p1 = P1[i]
            q1 = P1[0]
            p2 = P2[j]
            q2 = P2[0]
            
            if doIntersect(p1, q1, p2, q2):
#                 print("Yes")
                flag = 1
#                 print(P1[i], P1[0])
#                 print(P2[j], P2[0])

        if flag:
            if doIntersect(p1, q1, p2, q2) == 1:
                if intPoint(p1,q1,p2,q2) not in points:
                    points.append(intPoint(p1,q1,p2,q2))
            
# print(points,'\n')

# finding the points inside polygon
for pt in P2:
    if (rIntersection(P1, pt) and lIntersection(P1, pt)):
        if pt not in points:
            points.append(pt)
            
for pt in P1:
    if (rIntersection(P2, pt) and lIntersection(P2, pt)):
        if pt not in points:
            points.append(pt)

print('points: ', points)

# Arranging points to form polygon
# points = [(0.0, 25.0), (12.307692307692308, 15.384615384615385), (-12.5, 25.0), (-15.333333333333334, 19.333333333333332), (10, 20)]

l = len(points)
p = points[0]
for pt in points:
    if pt[0] == p[0] and pt[1] < p[1]:
        pr = points.pop(points.index(p))
        p = pt 
        
    elif pt[0] < p[0]:
        p = pt
# print(p)           
points.remove(p)
# print(points)
slope = []
sequence = []
for pt in points:
    s = (pt[1]-p[1])/(pt[0]-p[0])
    slope.append(s)

sequence = ([x for _, x in sorted(zip(slope, points))])
sequence.insert(0, p)
if len(sequence) != l:
    sequence.append(pr)
print("New Sequence of points: ", sequence)

# Finding area of polygon
sum = 0
for i, p in enumerate(sequence):
    if p == sequence[-1]:
        sum += (sequence[i][0]*sequence[0][1] - sequence[0][0]*sequence[i][1])
    else:
        sum += (sequence[i][0]*sequence[i+1][1] - sequence[i+1][0]*sequence[i][1])
        
area = sum/2
print('Area = {} squared units'.format(area))
