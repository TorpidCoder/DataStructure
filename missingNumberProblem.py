__author__ = "ResearchInMotion"

nums = [9,6,4,2,3,5,7,0,1]


def missingNumber(nums):
    for value in range(0, len(nums) + 1):
        if value not in nums:
            return value


print(missingNumber(nums))
