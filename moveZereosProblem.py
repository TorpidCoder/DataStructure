__author__ = "ResearchInMotion"


# def moveZereos(arr):
#     zeroArr = []
#     numArr = []
#     mainArr = []
#
#     for i in arr:
#         if i == 0:
#             zeroArr.append(i)
#         else:
#             numArr.append(i)
#     mainArr = numArr + zeroArr
#
#     return mainArr
#
# print(moveZereos(arr=[0,1,0,3,12]))

def moveZeroes(nums):
    zeroArr = []
    numArr = []
    mainArr = []

    for i in nums:
        if i == 0:
            zeroArr.append(i)
        else:
            numArr.append(i)
    mainArr = numArr + zeroArr

    return mainArr

print(moveZeroes(nums=[0,1,0,3,12]))

def moveZereos(arr):
    i = 0
    j = 1
    while j < len(arr):
        if arr[i] == 0:
            arr[i] , arr[j] = arr[j] , arr[i]
        if arr[i] != 0:
            i+=1
        j +=1
    return arr


print(moveZereos(arr=[0,1,0,3,12]))





