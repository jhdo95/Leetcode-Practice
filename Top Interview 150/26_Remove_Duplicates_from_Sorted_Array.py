"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # Check if nums is empty
            return 0
        
        k = 1  # Initialize index k to 1 (assuming the first element is always unique)
        for i in range(1, len(nums)):  # Iterate through the array starting from index 1
            if nums[i] != nums[k - 1]:  # If current element is not equal to the element at index k-1
                nums[k] = nums[i]  # Move it to index k
                k += 1  # Increment k
        return k  # Return k as the number of unique elements
    
"""
To solve this problem, we can use a two-pointer approach similar to the previous problem. We'll have one pointer (i) iterate through the array, and another pointer (k) keep track of the index where we can place unique elements.

Here's how we can approach the solution:

Initialize k to 0. This will represent the index where we'll place unique elements.

Iterate through the array with a pointer i. For each element nums[i]:

If nums[i] is not equal to the element at index k, we'll move it to index k and increment k.
If nums[i] is equal to the element at index k, we'll skip it.
Once we've iterated through the array, k will represent the number of unique elements in the modified array.

Finally, we'll return k, which represents the number of unique elements in nums.

Let's implement this in Python:^^

This solution modifies the input array in-place, ensuring that the first k elements contain only unique elements. Finally, it returns k, which represents the number of unique elements in nums.
"""