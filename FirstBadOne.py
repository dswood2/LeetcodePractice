"""

You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all 
the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 
Constraints:
1 <= bad <= n <= 231 - 1

"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    
    def firstBadVersion(self, n: int) -> int:
        start = 1 #initiate starting pointer
        end = n #initiate ending pointer
        if isBadVersion(1):#if only one, itself has to be bad
            return 1
        if isBadVersion(n) and not isBadVersion(n-1): #takes care of certian cases 
            return n
        while start + 1 < end: #while start is still in front of end
            mid = (start+end)//2 #divide data in half
            if not isBadVersion(mid): #True if mid is false (not bad)
                start = mid
            else: #True if mid is true (is bad) moves pointer around like above
                end = mid
            if isBadVersion(mid) and not isBadVersion(mid-1): #checks to see if we get our answer
                return mid
        
def isBadVersion(self, n:int) -> bool:
    print()#makes swiggly line go away

"""
Faster and another solution

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
        

"""