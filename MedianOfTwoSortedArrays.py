"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = [] 
        while True: # starting loop
            if nums1 == []: # if empty add the other array to merged
                merged += nums2
                break
            elif nums2 == []:
                merged += nums1
                break
                
            if nums1[0] > nums2[0]: #compare the two numbers
                merged.append(nums2.pop(0))
            else:
                merged.append(nums1.pop(0))

        lengthMerged = len(merged)
        if lengthMerged%2 != 0: # if length is odd
            return merged[lengthMerged//2]
        return (merged[lengthMerged//2-1] + merged[lengthMerged//2])/2

test=Solution
print(test.findMedianSortedArrays(test,[1,3],[2,4,5]))
            
        