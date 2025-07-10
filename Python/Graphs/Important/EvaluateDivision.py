'''
Link : https://leetcode.com/problems/evaluate-division/
Reference : https://www.youtube.com/watch?v=Uei1fwDoyKk
Company : Meta
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for i, ele in enumerate(equations):
            a,b = ele
            graph[a].append([b, values[i]]) # Multiply a by b
            graph[b].append([a, 1 / values[i]]) # Divide b by a (inverse)

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1

            queue = deque()
            visit = set()
            queue.append([src, 1])
            visit.add(src)

            while queue:
                ele, w = queue.popleft()

                if ele == target:
                    return w
                for neighbour, weight in graph[ele]:
                    if neighbour not in visit:
                        queue.append([neighbour, w * weight])
                        visit.add(neighbour)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
            

        