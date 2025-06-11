'''
Link : https://leetcode.com/problems/linked-list-cycle-ii/submissions/1660354341/?envType=problem-list-v2&envId=linked-list
We're using both set and linkedlist concepts in this question
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        seen = set()

        while curr:
            if (curr in seen):
                return curr
            else: 
                seen.add(curr)
                curr = curr.next
        return None