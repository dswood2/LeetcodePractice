"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def recursive(n):
            if n <= 2:
                return n
            if n in dp:
                return dp[n] 
            else: 
                dp[n] = recursive(n-1) + recursive(n-2)
                return dp[n]
        return recursive(n)

test = Solution()
n = 2 
print(test.climbStairs(n))



"""
        
Another way to think about these
class Solution:
    def climbStairs(self, n: int) -> int:
        
        one = 1
        two = 2
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for i in range(3, n+1):
            one, two = two, one+two
        
        return two        
        
    
"""
       