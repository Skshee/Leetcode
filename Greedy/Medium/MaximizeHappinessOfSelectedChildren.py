'''
Link : https://leetcode.com/problems/maximize-happiness-of-selected-children/
Time Complexity : O(n log n)
Topic : Greedy, Arrays
LeetCode Problem: 2680. Maximize Happiness of Selected Children
Solved question but I had complexity of O(n^2) initially so couldn't pass all test cases.
'''

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        maxSum = 0
        dec = 0   # tracks how many times we "would have" decremented

        while k and happiness:
            val = happiness[-1] - dec
            if val <= 0:
                break

            maxSum += val
            happiness.pop()   # instead of slicing
            dec += 1
            k -= 1

        return maxSum

        


        