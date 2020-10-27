__author__ = "ResearchInMotion"

# Write a Python program to sum all the items in a dictionary.
dicto = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
sum = 0
for values in dicto.values():
    sum += values

print(sum)
