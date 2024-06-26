"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:(picture on leetcode)


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Example 2:(picture on leetcode)


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

solution = Solution()

# Test Case 1
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix1)
print(matrix1)  # Output should be [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

# Test Case 2
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix2)
print(matrix2)  # Output should be [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]