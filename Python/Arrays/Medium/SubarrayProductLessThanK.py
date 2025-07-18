'''
Link : https://leetcode.com/problems/subarray-product-less-than-k/description/
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr=1
        left = right = 0
        ans = 0

        for right in range(len(nums)):
            curr *= nums[right]

            while curr >= k and left <= right:
                curr //= nums[left]
                left += 1
            
            ans += right - left + 1 # IMPORTANT STEP
        return ans



        