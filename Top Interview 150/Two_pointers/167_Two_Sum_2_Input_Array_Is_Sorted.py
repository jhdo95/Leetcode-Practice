"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
"""
To solve this problem, you can use a two-pointer approach since the input array is sorted. Here's how you can approach this:

Initialize two pointers, one at the beginning of the array (let's call it left) and the other at the end of the array (let's call it right).
While the left pointer is less than the right pointer, do the following:
Calculate the sum of the elements at the left and right pointers.
If the sum equals the target, return the indices left + 1 and right + 1.
If the sum is less than the target, move the left pointer to the right.
If the sum is greater than the target, move the right pointer to the left.
If no pair is found, return None or an empty list.

"""
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Adjust indices by 1 as per the problem statement
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        # If no solution found
        return None
solution = Solution()

# Test Case 1
numbers1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(numbers1, target1))  # Output should be [1, 2]

# Test Case 2
numbers2 = [2, 3, 4]
target2 = 6
print(solution.twoSum(numbers2, target2))  # Output should be [1, 3]

# Test Case 3
numbers3 = [-1, 0]
target3 = -1
print(solution.twoSum(numbers3, target3))  # Output should be [1, 2]