'''
Link : https://leetcode.com/problems/maximum-difference-between-increasing-elements/?envType=daily-question&envId=2025-06-16
'''

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1

        for num in nums[1:]:
            if(num > min_val):
                max_diff = max(max_diff, num - min_val)
            else:
                min_val = num
        return max_diff