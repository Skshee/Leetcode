'''
Link : https://leetcode.com/problems/word-search/
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Dimensions of the board
        rows, cols = len(board), len(board[0])

        # A set to keep track of visited cells in the current search path
        path = set()

        # Depth-First Search (DFS) function
        def dfs(r, c, i):
            # Base case: If we've matched all characters in word, return True
            if i == len(word):
                return True

            # Conditions to stop exploration:
            # 1. Out of bounds (r or c is invalid index)
            # 2. Current cell character doesn't match the word[i]
            # 3. Already visited this cell in the current path (avoid reuse)
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                board[r][c] != word[i] or 
                (r, c) in path):
                return False

            # Mark this cell as visited
            path.add((r, c))

            # Explore neighbors in 4 directions (down, up, right, left)
            res = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or 
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1))

            # Backtrack: unmark this cell so it can be used in another path
            path.remove((r, c))

            return res
        
        # Try to start DFS from each cell in the board
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):   # Start matching from word[0]
                    return True

        # If no path matches the word, return False
        return False
