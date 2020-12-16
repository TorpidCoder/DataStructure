__author__ = "ResearchInMotion"



duplicates = []
string = "My Name is Sahil Nagpal"
string = string.replace(" ","")
print(string)

for chars in string:
    if string.count(chars) > 1:
        duplicates.append(chars)

print(duplicates)

