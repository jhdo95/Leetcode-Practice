"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

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
Note that the second line is also left-justified because it contains only one word.
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
"""
Initialize variables to track the current line and its length.
Iterate through the words in words.
For each word, check if adding it to the current line will exceed maxWidth. If it does, we complete the current line and start a new line with the current word.
When completing a line, distribute the extra spaces between words evenly. If there's only one word on the line or it's the last line, left-justify it.
Repeat steps 3-4 until all words are processed.


We iterate through the words and greedily pack them into lines, ensuring each line has exactly maxWidth characters.
When completing a line, we distribute extra spaces between words evenly.
For the last line, we left-justify it instead of fully justifying it.
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        lines = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(word) + len(line) > maxWidth:
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '  # Distribute spaces evenly
                lines.append(''.join(line))
                line = []
                line_length = 0
                
            line.append(word)
            line_length += len(word)
            
        lines.append(' '.join(line).ljust(maxWidth))  # Left-justify the last line
        
        return lines

# Test cases
solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))