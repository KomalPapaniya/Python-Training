p1 = (5, 2)
p2 = (1, 6)

# p1 = (1, 2)
# p2 = (2, 5)

# p1 = (5, 2)
# p2 = (5, 7)

# p1 = (0, 10)
# p2 = (2, 0)

# p1 = (4, 8)
# p2 = (3, 8)

try:
    slope = (p2[1] - p1[1])/(p2[0] - p1[0])
    print("slope:", slope, end = ", ")
    y_intercept = p1[1] - slope*p1[0]
    print("y-intercept:", y_intercept)

    if p1[0] < p2[0]:
        x = p1[0] - 1

    else:
        x = p1[0] + 1

    y = slope * x + y_intercept

except ZeroDivisionError:
    x = p1[0]
    if p1[1] < p2[1]:
        y = p1[1] - 1
    else:
        y = p1[1] + 1        

# print('(',x,',',y,')')
print("Point in opposite direction: ({}, {})".format(x,y))