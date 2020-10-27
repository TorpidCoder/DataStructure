__author__ = "ResearchInMotion"
# Write a Python program to print all unique values in a dictionary. Go to the editor

dicto = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

print("Original List: ",dicto)

uniqDict = set(val for dic in dicto for val in dic.values())

print(uniqDict)
