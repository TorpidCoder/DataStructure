__author__ = "ResearchInMotion"

arr = [1,2,3,4,5]
rotation = int(input("Please enter the rotations : "))

# display the original array
print("The Actual Array is : ",arr)

# rotate the given array by n times
for i in range(0,rotation):
    # storing the first element of the array
    first = arr[0]

    for j in range(0,len(arr)-1):
        arr[j] = arr[j+1]

    arr[len(arr)-1] = first


print()

print("The length after rotation is : ",arr)






