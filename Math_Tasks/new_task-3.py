# Find area between 2 overlapping polygons (can be any type of polygon)
# polygon1 = [(-10, 30), (10, 20), (15, 10), (-20, 10)]
# polygon2 = [(-20, 25), (15, 25), (15, 15), (-20, 20)]
# Area = 172

P1 = [(-10, 30), (10, 20), (15, 10), (-20, 10)]
# P1 = [(0, 27), (15, 25), (15, 20)]
P2 = [(-20, 25), (15, 25), (15, 15), (-20, 20)]
# P1 = [(-30, 25), (-10, 10), (25, 20)]
# P2 = [(-20, 25), (5, 25), (4, 19), (-25, 5)]
# P1 = [(-20, 5), (15, 20), (15, -10), (-20, -10)]
# P2 = [(-20, 0), (5, 0), (5, -20), (-20, -20)]

INT_MAX = 10000
INT_MIN = -10000
points = []
        
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
        return True
 
    # Special Cases
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
 
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
 
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True

    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True

    return False

def intPoint(p1,q1,p2,q2):  # Using Cramer's Rule: https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
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
   

def isInside(points, p):
     
    n = len(points)
    r_extreme = (INT_MAX, p[1])
    l_extreme = (INT_MIN, p[1])
    i = 0
    r_flag = False
    l_flag = False

    while True:
        next = (i + 1) % n
        
        if r_flag == False:
            if (doIntersect(points[i], points[next], p, r_extreme)): 

                if orientation(points[i], p, points[next]) == 0:
                    return onSegment(points[i], p, points[next])              
                r_flag = True
            
        if l_flag == False:
            if (doIntersect(points[i], points[next], p, l_extreme)): 

                if orientation(points[i], p, points[next]) == 0:
                    return onSegment(points[i], p, points[next])              
                l_flag = True

        if r_flag and l_flag:
            return True
            
        i = next
        if (i == 0):
            break

    return False


for i in range(len(P1)):
    for j in range(len(P2)):
        flag = 0
        if i != len(P1) - 1 and j != len(P2) - 1:
            p1 = P1[i]
            q1 = P1[i+1]
            p2 = P2[j]
            q2 = P2[j+1]

            if doIntersect(p1, q1, p2, q2):
                flag = 1
            
        if i != len(P1) - 1 and j == len(P2) - 1:
            p1 = P1[i]
            q1 = P1[i+1]
            p2 = P2[j]
            q2 = P2[0]
            
            if doIntersect(p1, q1, p2, q2):
                flag = 1
                
        if i == len(P1) - 1 and j != len(P2) - 1:
            p1 = P1[i]
            q1 = P1[0]
            p2 = P2[j]
            q2 = P2[j+1]
            
            if doIntersect(p1, q1, p2, q2):
                flag = 1
                
        if i == len(P1) - 1 and j == len(P2) - 1:
            p1 = P1[i]
            q1 = P1[0]
            p2 = P2[j]
            q2 = P2[0]
            
            if doIntersect(p1, q1, p2, q2):
                flag = 1

        if flag:
            if doIntersect(p1, q1, p2, q2) == 1:
                if intPoint(p1,q1,p2,q2) not in points:
                    points.append(intPoint(p1,q1,p2,q2))
            
# print(points,'\n')

# finding the points inside polygon

for pt in P2:
    if isInside(P1, pt):
        if pt not in points:
            points.append(pt)
            
for pt in P1:
    if isInside(P2, pt):
        if pt not in points:
            points.append(pt)


print('\nPoints of overlapped Polygon:\n', points)

# Arranging points to form polygon

l = len(points)
p_min = points[0]
for pt in points:
    if pt[0] < p_min[0]:
        p_min = pt
    elif pt[0] == p_min[0] and pt[1] < p_min[1]:
        pr = points.pop(points.index(p_min))
        p_min = pt 
    elif pt[0] == p_min[0] and pt[1] > p_min[1]:
        pr = points.pop(points.index(pt))

# print(p_min)           
points.remove(p_min)
# print(points)
slope = []
sequence = []
for pt in points:
    s = (pt[1]-p_min[1])/(pt[0]-p_min[0])
    slope.append(s)

sequence = ([x for _, x in sorted(zip(slope, points))])
sequence.insert(0, p_min)
if len(sequence) != l:
    sequence.append(pr)
print('\nPoints after arranging in sequence:\n', sequence)


# Finding area of polygon
sum = 0
for i, p in enumerate(sequence):
    if p == sequence[-1]:
        sum += (sequence[i][0]*sequence[0][1] - sequence[0][0]*sequence[i][1])
    else:
        sum += (sequence[i][0]*sequence[i+1][1] - sequence[i+1][0]*sequence[i][1])
        
area = sum/2
print('\nArea of overlapped Polygon = {} squared units\n'.format(area))

# end = time.time()
# print(end - start)
