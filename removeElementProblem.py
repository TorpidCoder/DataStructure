__author__ = "ResearchInMotion"

nums = [3,2,2,3]
val = 3


def removeElement(arr,val):
    shift_spot = 0
    original_length = len(arr)
    for index in range(original_length):
        if arr[index] == val:
            shift_spot += 1
        else:
            arr[index-shift_spot] = arr[index]
    return original_length - shift_spot


print(removeElement(arr=nums,val=val))

