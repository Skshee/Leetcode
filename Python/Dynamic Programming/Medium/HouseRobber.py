'''
Link : https://leetcode.com/problems/house-robber/
Video Reference : https://www.youtube.com/watch?v=kIII1uT6F8Y
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i == 0:
                return nums[i]
            elif i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i]

            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]

        memo = {}
        return dp(len(nums) - 1)


            