__author__ = "ResearchInMotion"

nums1 = [1,2]
nums2 = [3,4]

def findMedianSortedArrays(nums1, nums2):
    mixedArray = nums1 + nums2
    mixedArray = sorted(mixedArray)
    medArr = sum(mixedArray) / len(mixedArray)
    return medArr

print(findMedianSortedArrays(nums1=nums1,nums2=nums2))