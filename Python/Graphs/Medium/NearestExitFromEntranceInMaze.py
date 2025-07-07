'''
Link : https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
'''

My Method:
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n

        queue = deque()
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        queue.append((entrance[0], entrance[1], 0))
        visited.add((entrance[0], entrance[1]))

        while queue:
            r, c, steps = queue.popleft()

            if (r, c) != (entrance[0], entrance[1]) and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                return steps

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if isValid(new_r, new_c) and maze[new_r][new_c] == '.' and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, steps + 1))

        return -1

Faster Method:

