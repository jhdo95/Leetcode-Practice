"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
"""
Convert the string s to lowercase.
Remove all non-alphanumeric characters from the string.
Check if the resulting string is equal to its reverse. If it is, return True; otherwise, return False.

We convert the string s to lowercase and remove all non-alphanumeric characters using a list comprehension.
Then, we check if the cleaned string is equal to its reverse. If it is, we return True; otherwise, we return False.
"""
class Solution:
    def isPalindrome(self, s):
        # Convert to lowercase and remove non-alphanumeric characters
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the cleaned string is equal to its reverse
        return clean_s == clean_s[::-1]

# Test cases
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))                     # Output: False
print(solution.isPalindrome(" "))                              # Output: True