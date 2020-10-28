__author__ = "ResearchInMotion"

arr = [25,54,32,5]


def minimumOfArray(arr):
    global min
    min = arr[0]
    for values in arr:
        if (min > values):
            min = values
    return min


print(minimumOfArray(arr=arr))



