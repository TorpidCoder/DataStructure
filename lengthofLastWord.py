__author__ = "ResearchInMotion"

s = "H"


def lengthWord(s):
    result = [x for x in s.split(" ")]
    index = len(result) - 1
    return len(result[index])


print(lengthWord(s))
