__author__ = "ResearchInMotion"
import math
nums = [1, 2, 3, 4]
newnums = []
maxval = max(nums)
for values in nums:
    if values < maxval:
        newnums.append(values)
for vals in newnums:
    if vals+vals > maxval:
        print("-1")
    else:
        print(maxval)

