"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
"""
To solve this problem efficiently, we can use a technique called the Boyer-Moore Voting Algorithm. This algorithm allows us to find the majority element in linear time complexity O(n) and constant space complexity O(1).

Here's how the Boyer-Moore Voting Algorithm works:

Initialize two variables: candidate and count. Set candidate to None and count to 0.
Iterate through the array nums. For each element:
If count is 0, set the current element as the candidate and increment count.
If the current element is equal to the candidate, increment count.
If the current element is different from the candidate, decrement count.
After iterating through all elements, the candidate variable will hold the majority element.
Let's implement this algorithm:
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
    

"""
Explanation:
We iterate through the array nums.
If count is 0, we set the current element as the candidate because it is the only element seen so far.
If the current element is equal to the candidate, we increment count because it is likely to be a majority element.
If the current element is different from the candidate, we decrement count because it is likely to cancel out the count of the majority element.
After iterating through all elements, the candidate variable holds the majority element.
This algorithm works because the majority element appears more than ⌊n / 2⌋ times. 
Therefore, even if the count is occasionally canceled out by other elements, the majority element's count will still remain positive in the end.
"""

def main():
    sol = Solution()
    # Test case 1
    nums1 = [3, 2, 3]
    print("Test case 1:")
    print("Input:", nums1)
    print("Expected Output: 3")
    print("Actual Output:", sol.majorityElement(nums1))
    print()
    
    # Test case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print("Test case 2:")
    print("Input:", nums2)
    print("Expected Output: 2")
    print("Actual Output:", sol.majorityElement(nums2))
    print()

    # Additional test cases
    nums3 = [1, 2, 3, 3, 3]
    print("Test case 3:")
    print("Input:", nums3)
    print("Expected Output: 3")
    print("Actual Output:", sol.majorityElement(nums3))
    print()

    nums4 = [1, 1, 2, 2, 3, 3, 3]
    print("Test case 4:")
    print("Input:", nums4)
    print("Expected Output: 3")
    print("Actual Output:", sol.majorityElement(nums4))
    print()

if __name__ == "__main__":
    main()