"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

"""
Keep track of the furthest reachable index (max_reach) and the current boundary of the current jump (curr_boundary). Initially, set both to 0.
Iterate over each index i from 0 to n-1 (where n is the length of the input array nums).
While iterating, update max_reach to be the maximum of max_reach and i + nums[i], which represents the furthest index you can reach from the current index i.
If the current index i is equal to curr_boundary, it means you have reached the boundary of the current jump. Increment the jump count and update curr_boundary to max_reach.
If the max_reach is greater than or equal to n-1, you have reached the last index. Return the jump count.

"""
class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:  # If the array has only one element, no jumps needed
            return 0
        
        max_reach = 0
        curr_boundary = 0
        jumps = 0
        
        for i in range(n):
            max_reach = max(max_reach, i + nums[i])
            
            if i == curr_boundary:
                jumps += 1
                curr_boundary = max_reach
                
                if max_reach >= n - 1:  # If we've reached or passed the last index
                    return jumps
        
        return jumps
    
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [2, 3, 1, 1, 4]
    print(solution.jump(nums1))  # Expected output: 2

    # Test Case 2
    nums2 = [2, 3, 0, 1, 4]
    print(solution.jump(nums2))  # Expected output: 2

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    print(solution.jump(nums3))  # Expected output: 4