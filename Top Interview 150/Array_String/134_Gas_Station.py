"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
"""
"""
To solve this problem, we can utilize the concept of the gas station problem's solution which involves calculating the difference between 
the amount of gas available and the cost to travel to the next station. We iterate over the gas stations, starting from each station, and 
check if we can complete the circuit.
We initialize variables total_gas, total_cost, tank, and start_station. total_gas and total_cost are used to check if the total 
amount of gas available is greater than or equal to the total cost of traveling. tank represents the current amount of gas in the tank, 
and start_station stores the starting station index.

We iterate over the gas stations using a for loop. For each station, we update total_gas and total_cost with the amounts of gas and 
cost at that station. We also update tank by subtracting the cost of traveling from the available gas. If tank becomes negative at any point, 
it means we can't reach the next station from the current starting station, so we reset tank to 0 and update start_station to the next station.

After the loop, if total_gas is less than total_cost, it means there isn't enough gas to complete the circuit, so we return -1. 
Otherwise, we return the starting station index.

This solution runs in O(n) time complexity, where n is the number of gas stations, as we only iterate over the stations once. 
It also satisfies the constraint of not using extra space apart from a few variables.
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        total_cost = 0
        tank = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            # If tank becomes negative, reset the tank and start from the next station
            if tank < 0:
                tank = 0
                start_station = i + 1
        
        # If the total gas is less than the total cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        else:
            return start_station if start_station < len(gas) else -1

# Test cases
solution = Solution()
print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))  # Output: 3
print(solution.canCompleteCircuit([2,3,4], [3,4,3]))  # Output: -1
        
