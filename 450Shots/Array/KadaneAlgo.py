__author__ = "ResearchInMotion"

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
size = len(arr)


def maxSubArraySum(a, size):
    max_sofar = 0
    max_ending = 0

    for i in range(0,size):
        max_ending = max_ending + a[i]
        if max_ending < 0:
            max_ending = 0
        elif max_sofar < max_ending:
            max_sofar = max_ending
    return max_sofar

print(maxSubArraySum(a=arr,size=size))



