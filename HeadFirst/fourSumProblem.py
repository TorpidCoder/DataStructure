__author__ = "ResearchInMotion"



nums = [1,0,-1,0,-2,2]
target = 0

def fourSum(arr, target):
    nums.sort()
    result = set()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            for k in range(j + 1, len(nums) - 1):
                for l in range(k + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] + nums[l] == target):
                        result.add(tuple((nums[i], nums[j], nums[k], nums[l])))

    return result

print(fourSum(arr=nums,target=target))

