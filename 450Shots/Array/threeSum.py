__author__ = "ResearchInMotion"

arr = [1,2,3,4,5,6]
number = 13

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i] + arr[j] + arr[k] == number:
                print(arr[i],',',arr[j],',',arr[k])