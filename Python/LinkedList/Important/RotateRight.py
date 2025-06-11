# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        curr = head

        if not head or not head.next:
            return head

        length = 1  # Length = 1 because if we need to 0 it only counts n-1 nodes (numbers of nexts basically)
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head

        curr2 = head
        for i in range(length - k % length - 1): # This is part where I made a mistake
            curr2 = curr2.next
        head = curr2.next
        curr2.next = None
        return head
