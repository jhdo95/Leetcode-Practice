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
we should accumulate the profits from ascending sequences of prices. This means that whenever we encounter a price that is higher than the previous day, we should add the difference between the current and previous prices to the total profit.

Here's the revised approach:

Initialize Variables: Initialize a variable total_profit to keep track of the total profit. Set it to 0 initially.

Iterate Through Prices: Iterate through the prices array. For each pair of consecutive days:

If the current price is higher than the previous price, add the difference between the current and previous prices to total_profit.
Return Total Profit: After iterating through all prices, return total_profit.


"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variable
        total_profit = 0
        
        # Iterate through prices
        for i in range(1, len(prices)):
            # Add profit if the current price is higher than the previous price
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit

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