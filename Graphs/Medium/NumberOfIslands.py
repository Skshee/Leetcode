class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                r,c = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    if (r+dr) in range(rows) and (c+dc) in range(columns) and grid[r+dr][c+dc] == '1' and (r+dr, c+dc) not in visit:
                        visit.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc))


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

