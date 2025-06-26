'''
Link : https://leetcode.com/problems/range-sum-of-bst/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        def traversal(node):
            if not node:
                return 0

            if node.val >= low and node.val <= high:
                self.sum += node.val
                traversal(node.left)
                traversal(node.right)
            if node.val > high:
                traversal(node.left)
            if node.val < low:
                traversal(node.right)
        traversal(root)
        return self.sum
        