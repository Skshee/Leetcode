'''
Link : https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        self.count = 0

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        def dfs(i):
            for neighbour in graph[i]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                self.count += 1
            else:
                continue
        return self.count