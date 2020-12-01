__author__ = "ResearchInMotion"

arr = [2,6,4,1]


def threeConsecutiveOdds(arr):
    for values in range(len(arr) - 2):
        if arr[values] % 2 == 1 and arr[values + 1] % 2 == 1 and arr[values + 2] % 2 == 1:
            #print(arr[values], arr[values + 1], arr[values + 2])
            return True
            break
    else:
        return False


print(threeConsecutiveOdds(arr))
