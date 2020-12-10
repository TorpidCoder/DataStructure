__author__ = "ResearchInMotion"

arr =[0,1,2,3,4,5,6,66]


def maximum(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] >= max:
            max = arr[i]
    return max
# for maximum
print(maximum(arr))


def minimum(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] <= min:
            min = arr[i]
    return min
# for minimum
print(minimum(arr))
