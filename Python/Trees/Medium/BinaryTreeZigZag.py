'''
Link : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        queue = deque([root])
        res = []
        level = 0
        
        while queue:
            level_size = len(queue)
            inner = []
            for i in range(level_size):
                node = queue.popleft()
                inner.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                inner.reverse()
            res.append(inner)
            level += 1
        
        return res
        