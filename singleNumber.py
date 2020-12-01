__author__ = "ResearchInMotion"


from collections import Counter

nums = [2,2,1]


def singleNumber(nums):
    result = Counter(nums)
    for key, value in result.items():
        if value == 1:
            return key


print(singleNumber(nums))
