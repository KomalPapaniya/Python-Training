A = [ [2, 0, 7, -3],
      [4, 1, 9, 6],
      [8, 1, -1, 0], 
      [2, 21, 0, -8]
     ]
minor = 0
major = 0
for i in range(len(A)):
    major += A[i][i]
    minor += A[i][len(A)-i-1]
print("Sum of major diagonal = {0}\nSum of minor diagonal = {1}".format(major, minor))