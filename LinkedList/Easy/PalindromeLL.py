'''
Link : https://leetcode.com/problems/palindrome-linked-list/
Time Complexity : O(n)  
Space Complexity : O(n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        curr = head

        while curr:
            lst.append(curr.val)
            curr = curr.next

        n = len(lst)
        for i in range(n//2):
            if lst[i] != lst[n-i-1]:
                return False
        return True