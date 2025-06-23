# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            if node.left == None:
                return 1 + dfs(node.right)
            elif node.right == None:
                return 1 + dfs(node.left)
            else:
                return min(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
        