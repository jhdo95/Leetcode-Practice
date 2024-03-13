"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
"""
We iterate through the haystack string using a sliding window of length equal to the length of the needle string.

For each position of the sliding window, we check if the substring of the haystack starting from that position and of the same length as the needle string matches the needle string.

If we find a match, we return the index of the starting position of the matching substring.

If we reach the end of the haystack string without finding a match, we return -1.f
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0
        
        # Iterate through the haystack string using a sliding window
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring of haystack matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # If no match is found, return -1
        return -1

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))   # Output: 0
print(solution.strStr("leetcode", "leeto"))  # Output: -1