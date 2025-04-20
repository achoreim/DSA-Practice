"""
Medium
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/

Time for first solution: DNF
Time to compile all solutions and notes: 37:34
"""

"""
Problem Description:

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified
to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

"""
My First Solution: Only solved for rows and columns, does not solve for 3x3 boxes:

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Validate Rows:
        for x in board:
            y = Counter(x)
            for i in y:
                if (i != ".") and (y[i] > 1):
                    return False
        
        transpose_board = list(zip(*board))

        # Validate Columns:
        for x in transpose_board:
            y = Counter(x)
            for i in y:
                if (i != ".") and (y[i] > 1):
                    return False


        # Validate Boxes:


        # Return True
        return True

"""
Second Solution after watching Greg Hogg's Youtube Tutorial:
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Validate Rows:
        for x in board:
            y = Counter(x)
            for i in y:
                if (i != ".") and (y[i] > 1):
                    return False
        
        transpose_board = list(zip(*board))

        # Validate Columns:
        for x in transpose_board:
            y = Counter(x)
            for i in y:
                if (i != ".") and (y[i] > 1):
                    return False


        starts = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)]


        # Validate Boxes:
        for x, y in starts:
            s = set()
            for row in range(x, x+3):
                for col in range(y, y+3):
                    if board[row][col] in s:
                        return False
                    else:
                        if board[row][col] != ".":
                            s.add(board[row][col])

        # Return True
        return True

"""
Notes:


    What I have learned:
        * You can Interate three at a time by manually coding a 'start' matrix as done here

    What I need to work on:
        * Better visualization of the problem, try to think in different angles.
"""