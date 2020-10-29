__author__ = "ResearchInMotion"

nums = [2,7,11,15]
target = 9


def twoSumOption1(arr , number):
    for values in range(len(nums)):
        if (nums[values - 1] + nums[values] == target):
            print(nums[values - 1], "and", nums[values], "makes", target)
    return "This is option 1"

def twoSumOption2(arr,number):
    dictonary = {}
    for newvalues in range(len(nums)):
        compliment = target - nums[newvalues]
        if compliment in dictonary:
            print(compliment, "and", nums[newvalues], "makes", target)
        dictonary[nums[newvalues]] = nums[newvalues]

    return "This is option 2"

# driver program
if __name__ == '__main__':


    print(twoSumOption1(nums,target))
    print(twoSumOption2(nums,target))














