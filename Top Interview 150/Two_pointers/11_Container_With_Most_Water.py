"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:
(PICTURE MISSING)

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the area between the lines represented by left and right pointers
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
solution = Solution()
# Test Case 1
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height1))  # Output should be 49

# Test Case 2
height2 = [1, 1]
print(solution.maxArea(height2))  # Output should be 1