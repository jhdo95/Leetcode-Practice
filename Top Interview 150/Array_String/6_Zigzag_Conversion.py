"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
"""
If numRows is 1 or if the length of the string s is less than or equal to numRows, return s itself, as there won't be any zigzag pattern to form.

Initialize a list of strings rows to store characters in each row of the zigzag pattern. The length of this list will be numRows.

Iterate through each character c in the string s and determine the row in which it should be placed based on the current position and direction in the zigzag pattern.

Append each character c to the appropriate row in the rows list.

After iterating through all characters, concatenate the strings in the rows list to form the final zigzag pattern.


This implementation correctly converts the input string s into a zigzag pattern with the given number of rows numRows. 
It handles cases where numRows is 1 or the length of s is less than or equal to numRows.
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If numRows is 1 or if the length of s is less than or equal to numRows, return s
        if numRows == 1 or len(s) <= numRows:
            return s

        # Initialize a list of strings to store characters in each row of the zigzag pattern
        rows = [''] * numRows

        # Initialize variables to track the current row and direction in the zigzag pattern
        current_row = 0
        going_down = False

        # Iterate through each character in the string s
        for char in s:
            # Append the current character to the appropriate row in the rows list
            rows[current_row] += char
            # Update the current row and direction based on the zigzag pattern
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Concatenate the strings in the rows list to form the final zigzag pattern
        zigzag_pattern = ''.join(rows)

        return zigzag_pattern

# Test cases
solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))              # Output: "A"