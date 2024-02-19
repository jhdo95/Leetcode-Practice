"""
Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

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

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
"""
To solve this problem, we'll use a two-pointer approach similar to previous solutions. We'll have one pointer iterate through the array to identify the unique elements, while another pointer keeps track of where to place these unique elements.

Here's how we can approach the solution:

Initialize two pointers: k and i. k will represent the position where we can place unique elements, and i will iterate through the array to identify unique elements.

Start iterating through the array from index 2 (since the first two elements are always considered unique in this case). For each element nums[i]:

If nums[i] is different from the two elements preceding it (nums[k - 1] and nums[k - 2]), we can consider it a unique element. Move it to index k and increment k.
Finally, return k, which represents the length of the modified array.

Let's implement this solution:
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)  # If there are 0 or 1 elements, no duplicates to remove
        
        k = 2  # Initialize the position for unique elements (first two elements are always unique)
        
        for i in range(2, len(nums)):  # Start iterating from index 2
            if nums[i] != nums[k - 1] or nums[i] != nums[k - 2]:
                # If current element is different from the two preceding elements, it's unique
                nums[k] = nums[i]  # Move it to index k
                k += 1  # Increment k
        
        return k  # Return the length of the modified array
"""
This solution modifies the input array in-place, ensuring that each unique element appears at most twice. 
Finally, it returns k, which represents the length of the modified array.
"""
# Test function
def test(nums):
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print("Output:", k, ", nums =", nums[:k])

# Test cases
test([1,1,1,2,2,3])
test([0,0,1,1,1,1,2,3,3])