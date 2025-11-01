'''
Link : https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2025-11-01
Time Complexity : O(N + M) where N is the length of linked list and M is the length of nums array
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        isPresent = set()

        for num in nums:
            if num not in isPresent:
                isPresent.add(num)

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val in isPresent:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return dummy.next
                


        