__author__ = "ResearchInMotion"

arr = [1,2,3,4,5]
arr2 = [5,6,7,8,9,2]
# intersection
# option -1
intersection = [values for values in arr if values in arr2]
print(intersection)

# option -2
intersection2 = set(arr).intersection(arr2)
print(list(intersection2))

# option -3
result = list(filter(lambda x : x in arr , arr2))
print(result)

# union
union = [values for values in arr2 if values not in arr]
print(union)


