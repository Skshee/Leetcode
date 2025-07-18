# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        if not head.next:
            return head.val

        length = 1
        ptr = head # To not change the actual position of head but traverse through LL, use ptr
        while ptr.next:
            length += 1
            ptr = ptr.next

        Sum = 0
        while head:
            Sum += head.val * (2**(length-1))
            head = head.next
            length -= 1
        
        return Sum

        