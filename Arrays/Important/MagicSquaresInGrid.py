'''
Link : https://leetcode.com/problems/magic-squares-in-grid/
840. Magic Squares In Grid
Medium
Challenges Faced : 1 - Row and Column sum check 2 - Unique number check
'''
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        for i in range(n-2):
            for j in range(m-2):
                # grid[i:i+3] → selects 3 rows
                # row[j:j+3] → selects 3 columns from each row
                newGrid = [row[j:j+3] for row in grid[i:i+3]]
                rowSum = [0] * 3
                colSum = [0] * 3
                diagonal = 0
                reverseDiagonal = 0

                nums = set()
                for r in range(3):
                    for c in range(3):
                        nums.add(newGrid[r][c])
                if nums != set(range(1, 10)):
                    continue
                
                for k in range(3):
                    rowSum[k] = sum(newGrid[k][0:3])
                    # Made mistake in the bottom line
                    colSum[k] = sum(newGrid[r][k] for r in range(3))
                    diagonal += newGrid[k][k]
                    reverseDiagonal += newGrid[k][2-k]

                if rowSum[0] == rowSum[1] == rowSum[2] == colSum[0] == colSum[1] == colSum[2] == diagonal == reverseDiagonal:
                    res+=1
        return res