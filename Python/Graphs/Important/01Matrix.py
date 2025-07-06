'''
Link : https://leetcode.com/problems/01-matrix/
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        def isValid(r,c):
            return 0<=r<rows and 0<=c<cols

        visited = set()
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c,1))
                    visited.add((r,c))

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        while queue:
            r,c, steps = queue.popleft()

            for dr, dc in directions:
                if (r+dr, c+dc) not in visited and isValid(r+dr, c+dc):
                    queue.append((r+dr, c+dc, steps + 1))
                    visited.add((r+dr, c+dc))
                    mat[r+dr][c+dc] = steps
        return mat

