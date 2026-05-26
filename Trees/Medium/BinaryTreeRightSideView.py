'''
Link : https://leetcode.com/problems/binary-tree-right-side-view/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []

        while queue:
            nodes_in_curr_level = len(queue)
            for i in range(nodes_in_curr_level):
                node = queue.popleft()

                if i == nodes_in_curr_level - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

        