"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

"""
Trim any trailing whitespace from the input string s using the strip() method. This ensures that we handle cases where there might be extra spaces at the end of the string.

Split the string into words using the split() method. This will create a list of words from the string, where each word is separated by whitespace.

If the resulting list of words is not empty, return the length of the last word in the list using the len() function.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Trim trailing whitespace and split the string into words
        words = s.strip().split()
        
        # Check if the list of words is not empty
        if words:
            # Return the length of the last word
            return len(words[-1])
        else:
            return 0  # If the list is empty, return 0

# Test cases
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))              # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))    # Output: 6
