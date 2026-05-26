# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q: # If either p or q is root, then lowest ancestor is the root itself
        
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q) 

        if left and right: # If p and q exist in left and right subtree, root is common ancestor
            return root

        if left: # If both p and q are in left subtree, return left
            return left

        return right # If both p and q are in right subtree, return right