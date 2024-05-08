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
        best_len = 0
        found_set = set()
        start = 0

        for end in range(len(s)): # Go through each letter in the string
            while s[end] in found_set: # Looking to see if current letter is in our hash table
                print("startt",start)
                print(s[start])
                print("s",s)
                print("found",found_set)
                found_set.remove(s[start]) # if so that means we have found duplicate and we can delete everything in or hash table up to and including current letter
                start+=1 # Moves our sliding window
            best_len = max(best_len, end-start+1) # get largest length
            found_set.add(s[end]) # add the current letter to the hash table
        return best_len

test = Solution
print(test.lengthOfLongestSubstring(test, "pwwkew"))

"""
Time complexity is O(n).  We only check each character once
Space Complexity is O(1).  Worst case would be where we have to store all the characters
"""