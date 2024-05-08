"""
Given an array of strings words and a width maxWidth, 
format the text such that each line has exactly maxWidth 
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; 
that is, pack as many words as you can in each line. Pad extra spaces ' ' 
when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 
Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        def test_line(line):
            return len(' '.join(line))<=maxWidth
        def make_spacing(line, isLastLine):
            if isLastLine or len(line)==1:
                spaced_str = " ".join(line)
                right_padding = " " * (maxWidth-len(spaced_str))
                return spaced_str+right_padding
            len_single_spaced = len(" ".join(line))
            dis_spaces = ((maxWidth-len_single_spaced)//(len(line)-1))+1
            extra_spaces = (maxWidth-len_single_spaced)%(len(line)-1)
            line = [word + " " * dis_spaces if i < len(line)-1 else word for i, word in enumerate(line)]
            if extra_spaces == 0:
                return "".join(line)
            line = [word + " " if i < extra_spaces else word for i, word in enumerate(line)] 
            return ''.join(line)
        while words:
            line = []
            while words and test_line(line + [words[0]]):
                line.append(words.pop(0))
            lines.append(make_spacing(line, not bool(words)))
        return lines
test = Solution()
testSet=["This", "is", "an", "example", "of", "text", "justification."]
testWidth=16
print(test.fullJustify(testSet,testWidth))