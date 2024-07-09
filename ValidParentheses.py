'''
Given a string s containing just the characters: 
    '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
* 1 <= s.length <= 10^4
* s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False
        
        return stack == []

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.isValid("()"))  # Expected: True
    
    # Test case 2
    print(solution.isValid("()[]{}"))  # Expected: True
    
    # Test case 3
    print(solution.isValid("(]"))  # Expected: False
    
    # Additional test cases
    print(solution.isValid("([)]"))  # Expected: False
    print(solution.isValid("{[]}"))  # Expected: True
    print(solution.isValid(""))  # Expected: True
    print(solution.isValid("(("))  # Expected: False