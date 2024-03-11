"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""
"""
Trim leading and trailing spaces from the string to handle cases where there might be leading or trailing spaces.

Split the string into words based on whitespace. This will create a list of words.

Reverse the list of words.

Join the reversed list of words into a single string with a single space between each word.

This implementation correctly reverses the order of words in the input string s. 
It handles cases where there might be leading or trailing spaces, as well as cases where there are multiple spaces between words.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Trim leading and trailing spaces and split the string into words
        words = s.strip().split()

        # Reverse the list of words
        reversed_words = words[::-1]

        # Join the reversed list of words into a single string with a single space between each word
        reversed_string = ' '.join(reversed_words)

        return reversed_string

# Test cases
solution = Solution()
print(solution.reverseWords("the sky is blue"))       # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))      # Output: "world hello"
print(solution.reverseWords("a good   example"))     # Output: "example good a"