__author__ = "ResearchInMotion"

arr = [23,56,27,54]
k =2

def largestElement(arr,k):
    arr=sorted(arr,reverse=True)
    return arr[k-1]

print(largestElement(arr,k))
