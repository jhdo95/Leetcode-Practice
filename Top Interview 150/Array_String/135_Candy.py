"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""

"""
To solve this problem, we can traverse the ratings array twice: once from left to right and once from right to left. 
In each traversal, we ensure that for each child, the number of candies they receive satisfies both conditions:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
"""
"""
Explanation:
We initialize an array candies with length n, where each element is initialized to 1, representing the minimum number of candies each child must have initially.

We traverse the ratings array from left to right and update the candies array based on the ratings. 
If the rating of the current child is greater than the rating of the previous child, we give them one more candy than the previous child.

We then traverse the ratings array from right to left and update the candies array again. If the rating of the current child is greater than the rating of the next child, 
we take the maximum of their current candy count and one more than the next child's candy count.

Finally, we return the sum of all elements in the candies array, which represents the minimum number of candies needed to distribute to the children while satisfying the given conditions.
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n  # Initialize candies array with 1 candy for each child
        
        # Traverse from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)

# Test cases
solution = Solution()
print(solution.candy([1,0,2]))  # Output: 5
print(solution.candy([1,2,2]))  # Output: 4