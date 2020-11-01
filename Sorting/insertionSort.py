__author__ = "ResearchInMotion"

def insertionSort(arr):
    indexing_len = range(1,len(arr))
    for i in indexing_len:
        values_sort = arr[i]
        while arr[i-1] > values_sort and i > 0:
                arr[i-1] , arr[i] = arr[i] , arr[i-1]
                i = i-1

    return arr

print(insertionSort(arr=[244,34,12,6,56]))

