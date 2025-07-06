'''
Link : https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # We have to solve this using graphs
        if k == 0:
            return [target.val]

        # Building the graph phase
        queue = deque()
        queue.append(root)
        graph = defaultdict(list)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right:
                queue.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        # Graph has been built, now time for the actual logic

        visited = set()
        visited.add(target.val)
        res = []
        queue2 = deque()
        queue2.append([target, 0])

        while queue2:
            node, distance = queue2.popleft()

            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge.val not in visited:
                        visited.add(edge.val)
                        queue2.append([edge, distance + 1])
        return res


                