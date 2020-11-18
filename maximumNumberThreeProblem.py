__author__ = "ResearchInMotion"

nums = [-1,-2,-3]
def maximumProduct(nums):
    nums.sort(reverse=True)
    negSum = -1
    if nums[-2] < 0 :
        negSum = nums[0] * nums[-1] * nums[-2]
    posSum = nums[0] * nums[1] * nums[2]
    return negSum if negSum > posSum else posSum


print(maximumProduct(nums))


