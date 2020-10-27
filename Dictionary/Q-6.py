__author__ = "ResearchInMotion"

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

start = int(input("Please enter the starting number : "))
end = int(input("Please enter the ending number : "))

dictionary = {}
for values in range(start,end+1):
    dictionary[values] = values*values

print(dictionary)

