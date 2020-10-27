__author__ = "ResearchInMotion"

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Enter the number : "))

# option1
newDict = {values: values*values for values in range(1,n+1)}
print(newDict)

# option2
newDict2 = {}
for values in range(1,n+1):
    newDict2[values] = values * values

print(newDict2)
