'''
https://leetcode.com/problems/odd-even-linked-list/
# Time: O(n)
# Space: O(1)
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even   # keep start of even list

        while even and even.next:
            odd.next = even.next   # odd skips over even
            odd = odd.next         # move odd forward
            even.next = odd.next   # even skips over odd
            even = even.next       # move even forward

        # attach even list after odds
        odd.next = even_head
        return head
