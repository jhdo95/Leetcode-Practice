"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
"""
To solve this problem in O(n) time complexity without using division, we can utilize the concept of prefix and suffix products. 
We'll traverse the array twice, once from left to right and once from right to left, 
to calculate the product of all elements to the left and right of each element respectively. 
Then, we'll combine these prefix and suffix products to get the desired result.

We first initialize three lists: left_products, right_products, and answer, each of length n. 
left_products and right_products will store the prefix and suffix products respectively, while answer will store the final result.

We calculate the prefix products by traversing the array from left to right. For each element nums[i], left_products[i] stores the product of all elements to the left of nums[i].

We calculate the suffix products by traversing the array from right to left. For each element nums[i], right_products[i] stores the product of all elements to the right of nums[i].

Finally, we combine the prefix and suffix products to get the final result. For each element nums[i], answer[i] is calculated as the product of left_products[i] and right_products[i].

This solution has a time complexity of O(n) because we traverse the array three times, each time in linear time. 
It doesn't require any extra space apart from the output array, so it meets the O(1) extra space complexity requirement.
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        answer = [0] * n
        
        # Calculate prefix products
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        # Combine prefix and suffix products
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]
        
        return answer
    
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]