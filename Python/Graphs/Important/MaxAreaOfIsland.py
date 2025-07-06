'''
Link : https://leetcode.com/problems/max-area-of-island/
Very Important Problem Frequently Asked in Google Interviews
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        def isValid(r,c):
            return 0<=r<m and 0<=c<n
        
        self.max_area = 0
        visited = set()
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))
            cur_area = 1
            
            while queue:
                r,c = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr,dc in directions:
                    if isValid(r+dr, c+dc) and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == 1:
                        cur_area += 1
                        visited.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc))
            self.max_area = max(self.max_area, cur_area)
                    
            
        
        m = len(grid)
        n = len(grid[0])
        
        for r in range(m):
            for c in range(n):
                if (r,c) not in visited and grid[r][c] == 1:
                    bfs(r,c)
        return self.max_area
                    