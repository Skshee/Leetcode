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
        avgs=[-1]*(n)
        left=0
        cur_sum = 0
        Range = 2*k+1
        for right in range(n):
            cur_sum += nums[right]
            while(right-left+1 == Range):
                avg = cur_sum//Range
                avgs[left+k] = avg
                cur_sum -= nums[left]
                left+=1
        return avgs

            

