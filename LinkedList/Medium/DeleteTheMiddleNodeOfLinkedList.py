'''
Link : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1 - My Method - Slower
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        curr = head
        middle = 0

        if(head.next == None):
            return None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            middle += 1

        count = 0
        while curr and curr.next:
            count +=1
            if(count == middle):
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
            

# Method 2 - Faster
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Delete the middle node
        slow.next = slow.next.next
        return dummy.next
    
    '''
    Why was a dummy node used?

    -> Since slow starts one node before head, you can safely do slow.next = slow.next.next for deletion — even if the node to be deleted is head. You simply return dummy.next — the new head of the list — whether or not the actual head was deleted.
    '''
