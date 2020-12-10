__author__ = "ResearchInMotion"

size1 , size2 , size3 = map(int,input("Please enter the input (comma seperted) : ").split(","))

# arr1
arr1= []
for i in range(size1):
    arr1.append(int(input("Enter the input element : ")))
print("The array 1 is :",arr1)

# arr 2
arr2= []
for i in range(size2):
    arr2.append(int(input("Enter the input element : ")))
print("The array 1 is :",arr2)

# arr 3
arr3= []
for i in range(size3):
    arr3.append(int(input("Enter the input element : ")))
print("The array 1 is :",arr3)

arr1 = set(arr1)
arr2 = set(arr2)
arr3 = set(arr3)

result = arr1.intersection(arr2).intersection(arr3)
print("The common element is : ",list(result))

