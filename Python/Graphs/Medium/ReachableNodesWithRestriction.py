class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen = set()
        graph = defaultdict(list)
        # IMP STEP Convert to set because set gives faster lookup (O(1)) instead of list ka (O(n))
        restricted_set = set(restricted)

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen and neighbour not in restricted_set:
                    seen.add(neighbour)
                    dfs(neighbour)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen.add(0)
        dfs(0)
        return len(seen)

        

        