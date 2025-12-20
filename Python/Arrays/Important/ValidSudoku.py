'''
Link: https://leetcode.com/problems/valid-sudoku/
Time Complexity : O(1) since the board size is fixed (9x9)
LeetCode Problem : 36. Valid Sudoku
Topic : Arrays, Hashing

'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]

        # Dealing with these subboxes is the only challenge in this problem
        subBoxSet = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in subBoxSet[r//3][c//3]:
                    return False

                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                subBoxSet[r//3][c//3].add(board[r][c])

        return True



        