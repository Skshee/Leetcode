'''
Link : https://leetcode.com/problems/all-paths-from-source-to-target/
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        path = [0]                       # start from source

        def dfs(u: int):
            if u == target:              # base case: reached target
                res.append(path[:])      # record a copy
                return
            for v in graph[u]:           # only expand neighbors of current node
                path.append(v)
                dfs(v)
                path.pop()               # backtrack

        dfs(0)
        return res
