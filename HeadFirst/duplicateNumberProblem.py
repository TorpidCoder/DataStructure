__author__ = "ResearchInMotion"

from itertools import count

nums = [1,3,4,2,2]


def findDuplicate(nums):
    for i in range(len(nums)):
        while nums[i] != nums[nums[i]]:
            num = nums[i]
            nums[i], nums[num] = nums[num], nums[i]

    return nums[0]

print(findDuplicate(nums))