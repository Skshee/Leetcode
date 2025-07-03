'''
https://leetcode.com/problems/find-if-path-exists-in-graph/
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        def dfs(node):
            if node == destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False

        graph = defaultdict(list)
        visited = set()

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        visited.add(source)
        return dfs(source)

        
            
        