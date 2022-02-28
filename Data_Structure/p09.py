string = "BCAHGBNAJKGTYUALKWG"
sub_seq = "AG"
count = 0
for i in string:
    if i == sub_seq[0] or i == sub_seq[1]:
        count += 1
print(count)