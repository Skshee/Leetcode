'''
Link : https://leetcode.com/problems/validate-binary-search-tree/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        values = []
        # Inorder traversal of BST is always sorted so just check that
        def inorderTraversal(node):
            if not node:
                return 

            left = inorderTraversal(node.left)
            values.append(node.val)
            right = inorderTraversal(node.right)
        inorderTraversal(root)
 
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False
        return True

        