"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
"""
Initialize two pointers, left and right, both pointing to the beginning of the array.
Keep moving the right pointer to the right until the sum of the elements between left and right is less than the target.
Once the sum is greater than or equal to the target, update the minimal length of the subarray found so far.
Move the left pointer to the right while updating the minimal length of the subarray until the sum is less than the target again.
Repeat steps 2-4 until the right pointer reaches the end of the array.
"""
class Solution(object):
    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0
        
        left = 0
        min_length = float('inf')
        current_sum = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0

solution = Solution()

# Test Case 1
target1 = 7
nums1 = [2, 3, 1, 2, 4, 3]
print(solution.minSubArrayLen(target1, nums1))  # Output should be 2

# Test Case 2
target2 = 4
nums2 = [1, 4, 4]
print(solution.minSubArrayLen(target2, nums2))  # Output should be 1

# Test Case 3
target3 = 11
nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
print(solution.minSubArrayLen(target3, nums3))  # Output should be 0