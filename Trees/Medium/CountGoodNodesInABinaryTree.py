'''
1448. Count Good Nodes in Binary Tree
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Medium
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxSoFar):
            if not node:
                return 0

            if node.val >= maxSoFar:
                maxSoFar = node.val
                goodCount = 1
            else:
                goodCount = 0

            left = dfs(node.left, maxSoFar)
            right = dfs(node.right, maxSoFar)
            return goodCount + left + right
        return dfs(root, float('-inf'))

            
        