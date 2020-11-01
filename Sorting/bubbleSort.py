__author__ = "ResearchInMotion"

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1] , arr[j]
    return arr


# driver code
print(bubbleSort(arr=[45,34,23,2,78]))
