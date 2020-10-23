__author__ = "ResearchInMotion"


def binarySearch(arr,low,high,number):

    # edge case
    # if length of the arr is less than 0


    if(high>=low):

        #calculate the mid element
        mid = int(low+(high-low)/2)

        if(arr[mid]==number):
            return mid
        elif(arr[mid]>number):
            return binarySearch(arr,low,mid-1,number)
        else:
            return binarySearch(arr,mid+1,high,number)
    else:
        return -1

if __name__ == '__main__':

    arr = []
    number = 12
    if (len(arr) <= 0):
        print("The array is empty")
    else:
        result = binarySearch(arr,0,len(arr)-1,number)
        if(result != -1):
            print("The number is present")
            print("The location is : " , result)
        else:
            print("The number is not present")






