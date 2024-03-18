"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
"""
To solve this problem, we can use a two-pointer approach. We'll iterate through both strings simultaneously, moving one pointer in each string. 
If the characters at the current positions of both pointers match, we'll advance both pointers. If not, we'll only advance the pointer in the longer string (t). 
If we reach the end of the substring s, it means s is a subsequence of t, and we return True. Otherwise, we return False.

We initialize two pointers, s_ptr and t_ptr, pointing to the start of strings s and t, respectively.
We iterate through both strings, comparing characters at the current positions of the pointers.
If characters match, we advance both pointers (s_ptr and t_ptr).
If characters don't match, we only advance the pointer in the longer string (t).
If we reach the end of s, it means s is a subsequence of t, so we return True. Otherwise, we return False.
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Pointers for both strings
        s_ptr = 0
        t_ptr = 0
        
        # Iterate through both strings
        while s_ptr < len(s) and t_ptr < len(t):
            # If characters match, advance both pointers
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            # Always advance the pointer in t
            t_ptr += 1
        
        # If s_ptr has reached the end of s, s is a subsequence of t
        return s_ptr == len(s)

solution = Solution()

# Example 1
print(solution.isSubsequence("abc", "ahbgdc"))  # Output: True

# Example 2
print(solution.isSubsequence("axc", "ahbgdc"))  # Output: False

# Additional test cases
print(solution.isSubsequence("ace", "abcde"))  # Output: True
print(solution.isSubsequence("aec", "abcde"))  # Output: False