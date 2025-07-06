'''
Link : https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1

        def isValid(r,c):
            return 0<=r<n and 0<=c<n

        visited = set()
        queue = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]

        def bfs(r,c,length):
            queue.append((r,c,length))
            visited.add((r,c))

            while queue:
                r,c,length = queue.popleft()

                if (r,c) == (n-1, n-1): # Imp step
                    return length

                for dr, dc in directions:
                    new_r = r+dr
                    new_c = c+dc

                    if isValid(new_r,new_c) and grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                        queue.append((new_r,new_c,length+1))
                        visited.add((new_r, new_c)) 
            return -1 # IMP

        return bfs(0,0,1)



