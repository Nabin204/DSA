#Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

#answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
#answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
#Note that the integers in the lists may be returned in any order.

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
        a = list(set(nums1).difference(set(nums2)))
        b = list(set(nums2).difference(set(nums1)))
        return [a,b]
lst1 = [2,4,0,7,9]
lst2 = [8,3,1,0,4]
print(findDifference(lst1,lst2))
