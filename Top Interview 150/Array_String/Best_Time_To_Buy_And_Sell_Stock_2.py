"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
"""

"""
To solve this problem, we need to find the maximum profit that can be achieved by buying and selling the stock. Since we can only hold at most one share of the stock at any time and we can buy and sell on the same day, we can consider every pair of consecutive days and calculate the profit if we buy on the first day and sell on the second day.

Here's how we can approach this problem:

Initialize Variables: Initialize a variable max_profit to keep track of the maximum profit achieved so far. Set it to 0 initially.

Iterate Through Prices: Iterate through the prices array. For each pair of consecutive days:

Calculate the profit if we buy on the current day and sell on the next day (prices[i + 1] - prices[i]).
Update max_profit to be the maximum of the current max_profit and the calculated profit.
Return Maximum Profit: After iterating through all pairs of consecutive days, return max_profit.

This implementation finds the maximum profit by considering every pair of consecutive days, 
making it efficient with a time complexity of O(n), where n is the length of the prices array.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variable
        max_profit = 0
        
        # Iterate through prices
        for i in range(len(prices) - 1):
            # Calculate profit for each pair of consecutive days
            profit = prices[i + 1] - prices[i]
            # Update max_profit
            max_profit = max(max_profit, profit)
        
        return max_profit

# Test cases
def main():
    sol = Solution()
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Test case 1:")
    print("Input:", prices1)
    print("Output:", sol.maxProfit(prices1))
    print()

    # Test case 2
    prices2 = [1, 2, 3, 4, 5]
    print("Test case 2:")
    print("Input:", prices2)
    print("Output:", sol.maxProfit(prices2))
    print()

    # Test case 3
    prices3 = [7, 6, 4, 3, 1]
    print("Test case 3:")
    print("Input:", prices3)
    print("Output:", sol.maxProfit(prices3))
    print()

if __name__ == "__main__":
    main()