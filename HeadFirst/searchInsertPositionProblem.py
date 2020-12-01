__author__ = "ResearchInMotion"


def searchInsert(nums, low, high, target):
    if (high >= low):
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return searchInsert(nums, low, mid - 1, target)
        else:
            return searchInsert(nums, mid + 1, high, target)

    else:
        return -1


# driver code
nums = [1,3,5,6]
target = 3
result = searchInsert(nums,0,len(nums)-1,target)
if result != -1:
    print("The element is present at",result, "index")
else:
    print("The element is not present")


