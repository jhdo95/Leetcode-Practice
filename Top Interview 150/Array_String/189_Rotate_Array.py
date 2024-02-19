"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Handle edge cases
        if not nums or k == 0:
            return
        
        # Reduce k to handle overflow
        k %= len(nums)
        
        # Rotate the array using array slicing
        nums[:] = nums[::-1]  # Reverse the entire array
        nums[:k] = nums[:k][::-1]  # Reverse the first k elements
        nums[k:] = nums[k:][::-1]  # Reverse the remaining elements

# Test cases
def main():
    sol = Solution()
    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print("Test case 1:")
    print("Input:", nums1, ", k =", k1)
    sol.rotate(nums1, k1)
    print("Output:", nums1)
    print()

    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    print("Test case 2:")
    print("Input:", nums2, ", k =", k2)
    sol.rotate(nums2, k2)
    print("Output:", nums2)
    print()

if __name__ == "__main__":
    main()