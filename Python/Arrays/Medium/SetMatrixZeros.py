'''
Link: https://leetcode.com/problems/set-matrix-zeroes/
Time Complexity : O(m * n)
Topic : Arrays, Hashing
LeetCode Problem : 73. Set Matrix Zeros
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeroRows, zeroCols = set(), set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)

        for r in range(m):
            for c in range(n):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0

        return matrix
        