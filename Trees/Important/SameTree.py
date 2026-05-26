'''
100. Same Tree
Link: https://leetcode.com/problems/same-tree/
Easy
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: both are None
        if not p and not q:
            return True

        # Case 2: one is None
        if not p or not q:
            return False

        # Case 3: values differ
        if p.val != q.val:
            return False

        # Case 4: check left and right subtrees
        return (
            self.isSameTree(p.left, q.left) and # self. because we are inside a class
            self.isSameTree(p.right, q.right)
        )
        


        