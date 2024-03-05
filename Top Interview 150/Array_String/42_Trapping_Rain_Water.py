"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

"""
To solve this problem, we can use a two-pointer approach to determine the amount of water trapped between the bars. Here's a step-by-step explanation of the algorithm:

Initialize two pointers, left and right, at the beginning and end of the height array respectively.

Initialize two variables, max_left and max_right, to keep track of the maximum height encountered from the left and right sides, initialized to 0.

Initialize a variable water to store the total amount of trapped water, initialized to 0.

While left is less than or equal to right, do the following:

If height[left] is less than or equal to height[right], meaning the height at the left pointer is less than or equal to the height at the right pointer:
    Check if height[left] is greater than max_left. If so, update max_left to height[left].
    Otherwise, calculate the amount of water trapped at the current position left as max_left - height[left], and add it to the water variable.
    Increment the left pointer.
If height[left] is greater than height[right], meaning the height at the left pointer is greater than the height at the right pointer:
    Check if height[right] is greater than max_right. If so, update max_right to height[right].
    Otherwise, calculate the amount of water trapped at the current position right as max_right - height[right], and add it to the water variable.
    Decrement the right pointer.
After the loop, return the total water trapped.

This solution traverses the array only once, hence it has a time complexity of O(n), where n is the number of elements in the height array. 
It utilizes constant space for storing variables left, right, max_left, max_right, and water, resulting in O(1) space complexity.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water = 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1
        
        return water

# Test cases
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(solution.trap([4,2,0,3,2,5]))  # Output: 9
