
'''
Link : https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
Time Complexity : O(n)
Topic : Linked List, Arrays
LeetCode Problem: 2130. Maximum Twin Sum of a Linked List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        curr = head
        maxTwinSum = 0

        while curr:
            lst.append(curr.val)
            curr = curr.next

        rev_lst = lst[-1::-1]

        for i in range(len(lst)):
            maxTwinSum = max(maxTwinSum, lst[i] + rev_lst[i])
        return maxTwinSum
        