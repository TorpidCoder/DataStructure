__author__ = "ResearchInMotion"

array = [1,2,3]


# option 1
def reverseArray(array):
    sizeofArray = len(array)
    higherIndex = sizeofArray - 1
    iterationsRequired = int(sizeofArray / 2)
    for i in range(0, iterationsRequired):
        temp = array[higherIndex]
        array[higherIndex] = array[i]
        array[i] = temp
        higherIndex -= 1
    return array

print(reverseArray(array))

# option 2
arr2=[1,2,3]
print(list(reversed(arr2)))

# option 3
arr3=[1,2,3]
arr3 = arr3[::-1]
print("The Third Options : ",arr3)

# option 4
arr4 = [1,2,3]
def reverseArrayValues(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr
print(reverseArrayValues(arr4,0,len(arr4)-1))
