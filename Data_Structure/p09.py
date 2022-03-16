# Count the subsequence “AG” in the given string.
# 			Ex. S = “BCAHGBNAJKGTYUALKWG”
# 			Output: 6

string = "BCAHGBNAJKGTYUALKWG"
sub_seq = "AG"
count = 0
for char in string:
    if char == sub_seq[0] or char == sub_seq[1]:
        count += 1
print(count)