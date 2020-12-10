__author__ = "ResearchInMotion"

arr = [-1,3,56,-2,34,1,-8]
negArr = []
posArr = []

for i in arr:
    if i < 0:
        negArr.append(i)
    else:
        posArr.append(i)
mainArr = posArr + negArr
print(mainArr)
