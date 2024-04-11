"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:(Picture on leetcode)

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:(Picture on leetcode)

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
"""
Iterate through each cell in the board.
For each cell, count the number of live neighbors.
Update the cell based on the rules provided.
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Helper function to count live neighbors
        def count_live_neighbors(board, i, j):
            count = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in [1, -1]:
                    count += 1
            return count
        
        # Iterate through each cell
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighbors = count_live_neighbors(board, i, j)
                
                # Apply the rules
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # mark for dead in next state
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2   # mark for live in next state
        
        # Update the board based on the marked cells
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

# Test cases
solution = Solution()
board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution.gameOfLife(board1)
print(board1)  # Output should be [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board2 = [[1,1],[1,0]]
solution.gameOfLife(board2)
print(board2)  # Output should be [[1,1],[1,1]]