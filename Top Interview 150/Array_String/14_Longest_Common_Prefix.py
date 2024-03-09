"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
"""
To solve this problem, we can compare the characters at corresponding positions in all the strings. 
The longest common prefix will be the substring that remains consistent across all strings until we encounter a character that differs. 

Initialize an empty string prefix to store the longest common prefix.

Iterate through the characters at each position in the first string (let's call it the reference string).

For each character position i:
Check if all other strings have the same character at position i. If they do, append the character to the prefix. If not, break out of the loop.
Return the prefix.
This implementation correctly finds the longest common prefix among the array of strings by comparing characters at corresponding positions. 
It iterates through each character position in the first string and checks if the character is common across all strings. If not, it returns the prefix found so far. 
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Check if the input list is empty
        if not strs:
            return ""

        # Initialize the longest common prefix as the first string
        prefix = strs[0]

        # Iterate through the characters of the first string
        for i in range(len(prefix)):
            # Check if the character at position i is common across all strings
            for s in strs[1:]:
                # If the current string is shorter than prefix or characters don't match, update prefix
                if i >= len(s) or prefix[i] != s[i]:
                    return prefix[:i]

        return prefix  # If all characters match, return prefix

# Test cases
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))     # Output: ""