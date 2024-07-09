'''
Maximum Subarray Problem

Given an integer array `nums`, find the subarray with the 
largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

'''

def maxSubArray(nums):
    '''
    
    Uses Kadane's algorithm.
        1. We start with both max_sum and current_sum equal to the first 
           element of the array.
        2. As we iterate through the rest of the array, for each element 
           we have two choices:
                a) Start a new subarray from this element 
                   (if current_sum becomes negative)
                b) Extend the current subarray by including this element
        3. The current_sum = max(num, current_sum + num) line makes 
           this decision. If current_sum becomes negative, it's better 
           to start a new subarray from the current element.
        4. We keep track of the maximum sum we've seen so far in 
           max_sum.

    This process ensures that we're always considering contiguous 
    subarrays. We're either extending the current subarray or starting 
    a new one, but never skipping elements or combining non-contiguous 
    parts.
    
    For example, in [-2,1,-3,4,-1,2,1,-5,4]:

    Start with -2
    Extend to [-2,1] (sum 1)
    Extend to [-2,1,-3] (sum -2)
    Start new subarray [4] (sum 4)
    Extend to [4,-1] (sum 3)
    Extend to [4,-1,2] (sum 5)
    Extend to [4,-1,2,1] (sum 6)
    Extend to [4,-1,2,1,-5] (sum 1)
    Extend to [4,-1,2,1,-5,4] (sum 5)

    The maximum sum found is 6, corresponding to the subarray [4,-1,2,1].
    '''
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases
test_cases = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [1],
    [5,4,-1,7,8]
]

for i, case in enumerate(test_cases, 1):
    result = maxSubArray(case)
    print(f"Test case {i}: {case}")
    print(f"Result: {result}\n")