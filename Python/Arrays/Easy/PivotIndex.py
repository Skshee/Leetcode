'''
Link to Problem: https://leetcode.com/problems/find-pivot-index/
Time Complexity : O(n)
Topic : Arrays, Prefix Sum
Leetcode Question Number : 724
'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)

        prefixSum = 0

        if prefixSum == totalSum - nums[0]:
            return 0
        
        for i in range(1,len(nums)):
            prefixSum += nums[i-1]
            print("Prefix Sum:",prefixSum)
            suffixSum = totalSum - prefixSum - nums[i]
            print("Suffix Sum:",suffixSum)

            if prefixSum == suffixSum:
                return i
        
        return -1
        