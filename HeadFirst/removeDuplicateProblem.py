__author__ = "ResearchInMotion"

nums = [0,0,1,1,1,2,2,3,3,4]

def uniqueList(arr):
    return list(set(sorted(arr)))

# driver program
if __name__ == '__main__':
    print(uniqueList(nums))


newarr = []
for values in range(len(nums)):
    if(nums[values] != nums[values-1]):
        newarr.append(nums[values])

print(newarr)

