class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # We can solve this using sliding window
        cur_sum, left = 0,0
        min_len = len(nums)+1
        for right in range(len(nums)):
            cur_sum += nums[right]
            while(cur_sum >= target): # Move the window till cur_sum < target
                length = right-left+1
                min_len = min(min_len,length)
                cur_sum -= nums[left]
                left+=1
        if (min_len == len(nums)+1):
            return 0
        else:
            return min_len