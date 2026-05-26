'''
Link : https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Trick is to calculate in-order traversal and then find diff of each adjacent elements in the array
        values = []
        def inorderTraversal(node):
            if not node:
                return

            left = inorderTraversal(node.left)
            values.append(node.val)
            right = inorderTraversal(node.right)
            
        inorderTraversal(root)
        min_diff = float('inf')
        for i in range(1,len(values)):
            min_diff = min(min_diff, values[i] - values[i-1])
        return min_diff
