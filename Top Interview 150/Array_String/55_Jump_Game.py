"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Initialize variable to store furthest reachable index
        max_reachable = 0
        
        # Iterate through nums array
        for i in range(len(nums)):
            # Check if current index is beyond the furthest reachable index
            if i > max_reachable:
                return False
            
            # Update furthest reachable index
            max_reachable = max(max_reachable, i + nums[i])
        
        # Check if furthest reachable index is greater than or equal to last index
        return max_reachable >= len(nums) - 1

# Test cases
def main():
    sol = Solution()
    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    print("Test case 1:")
    print("Input:", nums1)
    print("Output:", sol.canJump(nums1))
    print()

    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    print("Test case 2:")
    print("Input:", nums2)
    print("Output:", sol.canJump(nums2))
    print()

if __name__ == "__main__":
    main()