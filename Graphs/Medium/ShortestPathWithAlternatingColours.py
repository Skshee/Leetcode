'''
Link : https://leetcode.com/problems/shortest-path-with-alternating-colors/
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        # Build the graph
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)

        res = [-1] * n
        queue = deque()
        visited = set()

        # Starting from node 0 with both colors
        queue.append((0, 0, 'None'))  # (node, steps, last_color)
        visited.add((0, 'None'))

        while queue:
            node, steps, color = queue.popleft()

            # Only set result the first time we reach a node
            if res[node] == -1:
                res[node] = steps

            if color != 'Red':
                for nei in red[node]:
                    if (nei, 'Red') not in visited:
                        visited.add((nei, 'Red'))
                        queue.append((nei, steps + 1, 'Red'))

            if color != 'Blue':
                for nei in blue[node]:
                    if (nei, 'Blue') not in visited:
                        visited.add((nei, 'Blue'))
                        queue.append((nei, steps + 1, 'Blue'))

        return res
