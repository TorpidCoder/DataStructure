__author__ = "ResearchInMotion"

arr = [34,45,1,37,37,67,43]


def quickSort(mylist):
    if len(mylist) < 1 :
        return mylist
    else:
        pivot = mylist.pop()

    greaterlist = []
    lowerlist = []

    for value in mylist:
        if (value > pivot):
            greaterlist.append(value)
        else:
            lowerlist.append(value)

    return quickSort(lowerlist) + [pivot] + quickSort(greaterlist)

print(quickSort(arr))


