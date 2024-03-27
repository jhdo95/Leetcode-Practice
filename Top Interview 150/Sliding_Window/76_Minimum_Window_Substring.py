"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
"""
Create a hashmap char_count_t to store the frequency of characters in string t.
Initialize two pointers, left and right, both pointing to the beginning of string s.
Move the right pointer to the right until we find a window that contains all characters of t.
Once we find such a window, move the left pointer to the right until the window no longer contains all characters of t, but still maintains the minimum length.
Update the minimum window length and the corresponding indices.
Repeat steps 3-5 until the right pointer reaches the end of string s.
"""
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        char_count_t = Counter(t)
        required_chars = len(char_count_t)
        formed_chars = 0
        window_count = {}
        left = 0
        min_length = float('inf')
        min_window = ""

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            if char in char_count_t and window_count[char] == char_count_t[char]:
                formed_chars += 1
            
            while formed_chars == required_chars:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]

                char = s[left]
                window_count[char] -= 1
                if char in char_count_t and window_count[char] < char_count_t[char]:
                    formed_chars -= 1
                left += 1

        return min_window

solution = Solution()

# Test Case 1
s1 = "ADOBECODEBANC"
t1 = "ABC"
print(solution.minWindow(s1, t1))  # Output should be "BANC"

# Test Case 2
s2 = "a"
t2 = "a"
print(solution.minWindow(s2, t2))  # Output should be "a"

# Test Case 3
s3 = "a"
t3 = "aa"
print(solution.minWindow(s3, t3))  # Output should be ""