__author__ = "ResearchInMotion"

arr = [1,2,3,4,3,2,6,7]
duplicateElements = []

print("The duplicate elements are : ")
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i] == arr[j]):
            duplicateElements.append(arr[j])

print(duplicateElements)