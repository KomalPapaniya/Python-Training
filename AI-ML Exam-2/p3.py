nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # integer array
# nums = [-15, -2, -7]

sum_array = []  # array containing sum of all subarrays
for index_1 in range(len(nums)):
    for index_2 in range(index_1 + 1, len(nums)):
        sum_array.append(sum(nums[index_1:index_2+1]))
sum_array.extend(nums)  # for input array containing all negative values
print(max(sum_array))
