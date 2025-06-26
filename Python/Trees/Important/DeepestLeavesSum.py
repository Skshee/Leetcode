'''
Link : https://leetcode.com/problems/deepest-leaves-sum/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# METHOD 1 - BFS
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level_sum

    
# METHOD 2 - DFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.sum = 0
        self.max_depth = 0
        def dfs(node, depth):
            if not node:
                return 0
            
            
            if depth > self.max_depth:
                self.sum = node.val
                self.max_depth = depth
            elif depth == self.max_depth:
                self.sum += node.val
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
        dfs(root, 1)
        return self.sum

        
                