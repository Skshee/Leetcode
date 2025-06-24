'''
Link : https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            inner = []

            for _ in range(level_length):
                node = queue.popleft()
                inner.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(inner)
        return ans
        