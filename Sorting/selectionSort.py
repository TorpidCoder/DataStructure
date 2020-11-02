__author__ = "ResearchInMotion"

def selectionSort(arr):
    index_length = range(0,len(arr)-1)

    for i in index_length:
        min = i

        for j in range(i+1 , len(arr)):
            if(arr[j] < arr[min]):
                min = j

        if min != i:
            arr[min] , arr[i] = arr[i] , arr[min]

    return arr

print(selectionSort(arr=[23,13,56,34]))
