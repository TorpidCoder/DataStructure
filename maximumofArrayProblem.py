__author__ = "ResearchInMotion"


def maximumElement(arr):
    max = arr[0]
    for value in arr:
        if (value >= max):
            max = value
    return max


if __name__ == '__main__':
    arr = []
    size = int(input("Please enter the size of the Array : "))
    for numbers in range(0,size):
        arr.append(int(input("Please enter the element : ")))
    print("The array is :" , arr)
    print(maximumElement(arr))

