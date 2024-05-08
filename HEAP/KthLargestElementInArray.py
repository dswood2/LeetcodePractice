"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

"""

import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = [] 
        heapq.heapify(minHeap)
        for current in nums: #iterate through list
            if len(minHeap) < k: #creating a minHeap of length k
                heapq.heappush(minHeap, current)
            elif minHeap[0] < current:#pushing current value and popping min value. Keeps len k
                heapq.heappushpop(minHeap, current)
        return minHeap[0] # this value will be the kth largest since minHeap

test = Solution()
testList = [3,2,1,5,6,4]
k = 2
print(test.findKthLargest(testList,k))
