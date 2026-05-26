'''
Link : https://leetcode.com/problems/split-array-largest-sum/
Reference: https://www.youtube.com/watch?v=YUF3_eBdzsk
Complexity: O(nlog(sum(nums)))
Company : Amazon
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isValid(nums, mid, k):
            subarrays = 1 # By default we'll have atleast 1 subarray
            curSum = 0
            for n in nums:
                if curSum + n <= mid:
                    curSum += n
                else:
                    curSum = n
                    subarrays += 1
            return subarrays <= k

        left, right = max(nums), sum(nums) # Min value and Max value
        res = right

        while left <= right:
            mid = (left + right)//2

            if isValid(nums, mid, k):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

            

            