# Prefix Sum Method
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1]*n

        prefix = [0]*(n+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        for j in range(k,n-k):
            total = prefix[j+k+1]-prefix[j-k]
            avg = total//(2*k+1)
            res[j]=avg
        return res
            
# Sliding Window Method

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1]*n

        prefix = [0]*(n+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]+nums[i]
        for j in range(k,n-k):
            total = prefix[j+k+1]-prefix[j-k]
            avg = total//(2*k+1)
            res[j]=avg
        return res
            