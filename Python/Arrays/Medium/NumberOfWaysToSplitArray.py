# This is an example of Prefix Sum array questions
# Note : Avoid using sum method multiple time as it has high time complexity and the initial code I tried worked properly but time complexity was O(n^2)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        prefix_sum=0
        n = len(nums)
        count=0
        for i in range(n-1):
            prefix_sum += nums[i]
            suffix_sum = total_sum - prefix_sum
            if(prefix_sum >= suffix_sum):
                count+=1
        return count
