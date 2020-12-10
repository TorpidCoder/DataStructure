__author__ = "ResearchInMotion"

def smallestElement(arr,k):
    arr = sorted(arr)
    return arr[k-1]


arr = [23,56,27,54]
k =4
print(smallestElement(arr,k))
