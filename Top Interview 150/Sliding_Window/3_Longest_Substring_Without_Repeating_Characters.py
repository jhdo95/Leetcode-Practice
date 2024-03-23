"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
"""

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        char_index = {}  # Map to store the index of the characters
        
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

solution = Solution()

# Test Case 1
s1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(s1))  # Output should be 3

# Test Case 2
s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))  # Output should be 1

# Test Case 3
s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))  # Output should be 3