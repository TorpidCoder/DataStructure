__author__ = "ResearchInMotion"


arr = [1,3,5,2,4,6,87]
max = arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print("The maximum number is :" ,max)


fact = 1
for i in range(1,max):
    fact *= i
print("The factorial of ",max," is",fact)
