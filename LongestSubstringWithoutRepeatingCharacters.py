"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:    
        char_set = set()
        left = right = max_length = 0
        
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1
        
        return max_length

test = Solution
print(test.lengthOfLongestSubstring(test, "pwwkew"))

"""
This solution has a time complexity of O(n), where n is the length of 
the string, as we iterate through the string at most twice (once with 
the right pointer and once with the left pointer). The space complexity 
is O(min(m, n)), where m is the size of the character set, as we store 
at most min(m, n) characters in the set.

"""