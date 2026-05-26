class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        visited = set()
        restricted_set = set(restricted)

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in visited and neighbour not in restricted_set:
                    visited.add(neighbour)
                    dfs(neighbour)

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        visited.add(0)
        dfs(0)
        return len(visited)
        

