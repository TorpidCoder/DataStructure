__author__ = "ResearchInMotion"

import math
nums = [-2,1,-3,4,-1,2,1,-5,4]

sum = 0
max_sum = math.pow(-2,31) -1

for i in range(len(nums)):
    sum+=nums[i]
    max_sum = max(max_sum,sum)
    if sum < 0:
        sum = 0
print(max_sum)

