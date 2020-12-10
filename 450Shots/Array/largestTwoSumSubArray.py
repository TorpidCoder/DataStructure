__author__ = "ResearchInMotion"

arr = [2, 7, 11, 15, 6, 4]
maxElement = max(arr)

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == maxElement:
            print(arr[i], arr[j])
