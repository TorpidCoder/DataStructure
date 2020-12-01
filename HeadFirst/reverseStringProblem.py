__author__ = "ResearchInMotion"


string = "Hi My Name is Sahil"
values = [x[::-1] for x in string.split(" ")[::-1]]
print(" ".join(values))


new_string = []
index = len(string)
while index:
    index -= 1
    new_string.append(string[index])
print("".join(new_string))