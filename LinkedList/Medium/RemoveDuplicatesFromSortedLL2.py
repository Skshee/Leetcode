'''
Link : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Time Complexity : O(n)
Space Complexity : O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0,head)
        prev = dummy

        while curr:
            has_duplicate = False
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
                has_duplicate = True

            if has_duplicate:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        
        return dummy.next