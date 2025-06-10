'''
Link : https://leetcode.com/problems/swapping-nodes-in-a-linked-list/?envType=problem-list-v2&envId=linked-list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for i in range(k-1):
            curr = curr.next
        
        print(curr.val)
        right = curr
        left = head

        while curr.next:
            curr = curr.next
            left = left.next
        print(left.val)
            
        
        left.val,right.val = right.val, left.val
        return head

        