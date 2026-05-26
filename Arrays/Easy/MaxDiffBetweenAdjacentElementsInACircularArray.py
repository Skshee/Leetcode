class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = []
        n = len(nums)
        for i in range(n-1):
            diff.append(abs(nums[i+1]-nums[i])) 
        diff.append(abs(nums[0]-nums[n-1]))
        return max(diff)