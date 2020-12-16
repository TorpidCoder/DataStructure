__author__ = "ResearchInMotion"


arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
lowVal = 14
highVal = 20

lowArr = []
highArr = []

for i in arr:
    if i <= lowVal:
        lowArr.append(i)
    else:
        highArr.append(i)

lowArr = sorted(lowArr)
highArr = sorted(highArr)
mainArr = lowArr + highArr
print(mainArr)