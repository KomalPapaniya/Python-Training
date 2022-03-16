#  Find the intersection (common) of two sets and remove those elements from the first set.
# Sample: {23, 42, 65, 57, 78, 83, 29}
#         {57, 83, 29, 67, 73, 43, 48}
# Result: {57, 83, 29}, {65, 42, 78, 23}

set_A =  {23, 42, 65, 57, 78, 83, 29} 
set_B =  {57, 83, 29, 67, 73, 43, 48}
print(set_A & set_B,",", set_A - set_B)

# -------------------------------------------------------------

set_A =  {23, 42, 65, 57, 78, 83, 29}
set_B =  {57, 83, 29, 67, 73, 43, 48}
common = {x for x in set_A if x in set_A and x in set_B}
unique = {x for x in set_A if x in set_A and x not in set_B}
print(common, unique)