'''
Link : 
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Basically the min number of vertices required to reach all nodes would be equal to the total number of nodes whose indegree = 0
        indegree = [0] * (n)

        for _, y in edges:
            indegree[y] += 1

        return [node for node in range(n) if indegree[node] == 0]