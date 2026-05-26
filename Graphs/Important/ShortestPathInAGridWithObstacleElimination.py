'''
Link : https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
Reference : https://www.youtube.com/watch?v=VPleGcc1nZY&t=617s
'''

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])

        def isValid(r,c):
            return 0<=r<m and 0<=c<n

        visited = set()
        queue = deque()
        queue.append((0,0,0,k)) # Current Steps, Row, Column, Remaining Obstacles
        visited.add((0, 0, k)) # (Row, Column, Remaining Obstacles)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        while queue:
            steps,r,c,remaining = queue.popleft()
            
            if (r,c) == (m-1, n-1):
                return steps

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if isValid(new_r, new_c):
                    new_remaining = remaining - grid[new_r][new_c]
                    if new_remaining >= 0 and (new_r, new_c, new_remaining) not in visited:
                        visited.add((new_r, new_c, new_remaining))
                        queue.append((steps + 1, new_r, new_c, new_remaining))
        return -1

            

