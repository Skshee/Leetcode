class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        left = 0
        prefix_sum = [0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        for i in range(n):
            for j in range(i+2,n+1):
                sub_sum = prefix_sum[j] - prefix_sum[i]
                if (sub_sum % k == 0):
                    return True
        else:
            return False
        