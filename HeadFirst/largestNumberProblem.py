__author__ = "ResearchInMotion"


def largestNumber(nums):
    numstr = sorted([str(num) for num in nums])
    # go through the list to rearrage the order
    curr = [numstr[0]]
    for i in range(1, len(nums)):
        if curr[-1] + numstr[i] > numstr[i] + curr[-1]:
            numstr[i - len(curr)] = numstr[i]
            numstr[i] = curr[-1]
        elif curr[-1] + numstr[i] == numstr[i] + curr[-1]:
            curr.append(numstr[i])
        else:
            curr = [numstr[i]]

    result = ''.join(reversed(numstr))
    if int(result) > 0:
        return result
    else:
        return '0'


print(largestNumber([3,30,34,5,9]))

