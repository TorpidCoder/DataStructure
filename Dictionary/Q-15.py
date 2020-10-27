__author__ = "ResearchInMotion"

# Write a Python program to get a dictionary from an object's fields.

class myObject(object):
    def __init__(self):
        self.x = "red"
        self.y = "blue"
        self.z = "yellow"

test = myObject()
print(test.__dict__)
