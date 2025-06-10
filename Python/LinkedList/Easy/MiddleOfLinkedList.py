'''
Link : https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=problem-list-v2&envId=linked-list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        lst = []
        
        while fast and fast.next: 
            # When fast reaches the end, the slow would reach the middle
            slow = slow.next
            fast = fast.next.next
            
        while slow:
            lst.append(slow.val)
            return slow
            slow = slow.next