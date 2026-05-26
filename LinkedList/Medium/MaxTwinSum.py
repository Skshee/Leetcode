'''
Link : https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
Time Complexity : O(n)
Space Complexity : O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        lst = []
        maxSum = 0

        while curr:
            lst.append(curr.val)
            curr = curr.next

        n = len(lst)
        for i in range(n//2):
            maxSum = max(maxSum, lst[i] + lst[n-i-1])
        return maxSum
        