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
    
# Solution : 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]

        def dfs(node):
            if not node:
                return

            lca[0] = node
            if node is p or node is q:
                return 
            elif node.val < p.val and node.val < q.val:
                dfs(node.right)
            elif node.val > p.val and node.val > q.val:
                dfs(node.left)
            else:
                return 

        dfs(root)
        return lca[0]

# Solution 3 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root