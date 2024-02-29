"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 
Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

"""
1. Sort the citations array in non-decreasing order. This allows us to easily find the number of papers with at least h citations.
2. Initialize two pointers, left and right, where left starts at the beginning of the array, and right starts at the end.
3. Initialize a variable n to store the number of papers in the citations array.
4. Initialize a variable h_index to store the maximum h-index found so far.
5. Iterate through the sorted citations array:
    -Calculate the current h-index candidate as the minimum of the citation count and the number of papers remaining (n - left).
    -Update h_index to the maximum of its current value and the current h-index candidate.
    -Move the left pointer to the right until we find a citation count smaller than the current h-index candidate.
6. Return the h_index as the final result.

"""
class Solution(object):
    def hIndex(self, citations):
        citations.sort()  # Step 1
        n = len(citations)  # Step 3
        h_index = 0  # Step 4
        left, right = 0, n - 1  # Step 2
        
        while left <= right:  # Step 5
            h_candidate = min(citations[left], n - left)  # Step 5a
            h_index = max(h_index, h_candidate)  # Step 5b
            left += 1  # Step 5c
        
        return h_index  # Step 6
    
def test():
    sol = Solution()
    
    # Test case 1
    citations1 = [3, 0, 6, 1, 5]
    print("Input:", citations1)
    print("Output:", sol.hIndex(citations1))  # Expected output: 3
    
    # Test case 2
    citations2 = [1, 3, 1]
    print("Input:", citations2)
    print("Output:", sol.hIndex(citations2))  # Expected output: 1
    
    # Additional test cases
    citations3 = [0, 0, 0, 0, 0]
    print("Input:", citations3)
    print("Output:", sol.hIndex(citations3))  # Expected output: 0
    
    citations4 = [1, 2, 3, 4, 5]
    print("Input:", citations4)
    print("Output:", sol.hIndex(citations4))  # Expected output: 3
    
    citations5 = [5, 5, 5, 5, 5]
    print("Input:", citations5)
    print("Output:", sol.hIndex(citations5))  # Expected output: 5

# Run the test cases
test()