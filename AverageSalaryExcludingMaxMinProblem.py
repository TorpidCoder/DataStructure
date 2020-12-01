__author__ = "ResearchInMotion"

salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]

salary = sorted(salary)
salary.pop()
salary.pop(0)
sum = 0
for values in salary:
    sum+=values
result = sum/len(salary)
print(result)

print(sum(salary)-min(salary)-max(salary)/len(salary)-2)



