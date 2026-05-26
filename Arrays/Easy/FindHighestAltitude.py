'''
Link : https://leetcode.com/problems/find-the-highest-altitude/
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # We'll have to use prefix sum here
        n = len(gain)
        prefix_sum = [0]*(n+1)

        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + gain[i]
        return max(prefix_sum)