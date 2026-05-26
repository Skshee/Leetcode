'''
Link : https://leetcode.com/problems/reverse-nodes-in-k-group/
Time Complexity : O(n)
Space Complexity : O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        while count >= k:
            curr = prev.next
            nxt = curr.next

            for _ in range(1,k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            
            count -= k
            prev = curr
        
        return dummy.next