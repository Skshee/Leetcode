class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        Sum,ans = 0,0
        for i in nums:
            Sum += i
            ans = min(ans,Sum)
        return -ans+1