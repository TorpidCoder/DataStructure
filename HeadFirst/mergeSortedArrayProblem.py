__author__ = "ResearchInMotion"

a = [0,3,4,31]
b = [4,6,30]

c = a + b
for i in range(len(c)):
    for j in range(len(c)-i-1):
        if(c[i] > c[i+1]):
            c[i] , c[i+1] = c[i+1] , c[i]
print(c)