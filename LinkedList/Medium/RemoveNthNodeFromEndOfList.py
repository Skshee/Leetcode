'''
Link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        print(length)

        if(length == 1):
            head = None
        elif(length - n == 0):
            head = head.next
        else:
            left = head
            count = 0
            while left:
                count += 1
                if(count == length - n):
                    left.next = left.next.next
                else:
                    left = left.next
        return head

            