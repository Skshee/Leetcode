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
        # Iterate curr till k-1th index
        
        right = curr # Assigning the curr node to a new node called right. This is kth index to be swapped
        left = head


        while curr.next:
            curr = curr.next
            left = left.next
        
        # When curr reaches the end, left reaches the n-kth index therefore we swap left and right.
        
        left.val,right.val = right.val, left.val
        return head

        