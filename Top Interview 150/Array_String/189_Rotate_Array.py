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

"""
To solve this problem, we need to rotate the array to the right by k steps. There are multiple approaches to solve this problem, but one common approach involves using array slicing or reversing.

Here's a step-by-step process to solve this problem:

Handle Edge Cases: Check if the length of the array is 0 or if k is 0. If either condition is true, we don't need to perform any rotation, so we can return early.

Handle Overflow: Since rotating an array by its length results in the same array, we can reduce k to k % len(nums) to handle cases where k is greater than the length of the array.

Rotate the Array:

Approach 1: Use Array Slicing
Reverse the entire array.
Reverse the first k elements.
Reverse the remaining elements.
Approach 2: Use Array Slicing (Pythonic)
Assign nums to the result of slicing operation nums[-k:] + nums[:-k].
Approach 3: Use Extra Space
Create a new array and copy the elements in the rotated order.
Approach 4: Use Cyclic Replacements
Perform k cyclic replacements to move each element to its correct position.
Approach 5: Use Extra Space and Pop
Use the pop() method k times to remove the last element and insert it at the beginning.
Return: Depending on the approach used, we may or may not need to return anything. If the array is modified in-place, we don't need to return anything. Otherwise, we return the modified array.

Now, let's implement one of the approaches (Approach 1: Using Array Slicing) along with test cases:
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
"""
This implementation rotates the array in-place using array slicing and handles the provided test cases. 
"""