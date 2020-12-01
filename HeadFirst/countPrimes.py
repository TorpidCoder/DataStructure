__author__ = "ResearchInMotion"

n = int(input("Please enter the number : "))
count = 0

for values in range(n):
    if values <=1:
        continue
    for i in range(2,values):
        if(values%i) ==0:
            break
    else:
        count +=1
print(count)
