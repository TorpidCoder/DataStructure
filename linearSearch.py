__author__ = "ResearchInMotion"

def linearSearch(arr,number):
    for value in arr:
        if(number == value):
            return "The number is present at : " , arr[value]

    return "The number is not present"
# running the code
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    number = 3
    print(linearSearch(arr,number))