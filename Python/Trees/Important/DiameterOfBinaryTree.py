'''
Link : https://leetcode.com/problems/diameter-of-binary-tree/description/
Reference : https://www.youtube.com/watch?v=K81C31ytOZE
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        # Returns the current height
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.res = max(self.res, left + right) 
            
            return 1 + max(left, right) 
        dfs(root)
        return self.res
        