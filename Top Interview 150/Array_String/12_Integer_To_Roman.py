"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999

"""

"""
To solve the problem of converting an integer to a Roman numeral, we use a mapping between integer values and their corresponding Roman numeral symbols. The algorithm iteratively subtracts the largest possible integer values from the given number while appending the corresponding Roman numeral symbols to the result string. This ensures that the resulting Roman numeral string represents the given integer accurately.

The algorithm maintains the following steps:

Define a mapping between integer values and their corresponding Roman numeral symbols. This mapping is defined as a list of tuples, where each tuple contains an integer value and its corresponding Roman numeral symbol. The tuples are ordered in such a way that special cases like "IV" and "IX" are considered before the general cases.

Initialize an empty string result to store the resulting Roman numeral string.

Iterate through the mapping list:

While the given number num is greater than or equal to the current integer value in the tuple:
Append the corresponding Roman numeral symbol to the result string.
Subtract the current integer value from num.
Return the final result.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_mapping = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = ''
        
        for value, symbol in roman_mapping:
            while num >= value:
                result += symbol
                num -= value
        
        return result
# Test cases
solution = Solution()
print(solution.intToRoman(3))     # Output: "III"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"
