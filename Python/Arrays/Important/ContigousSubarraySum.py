'''
Link : https://leetcode.com/problems/continuous-subarray-sum/
Reference : https://www.youtube.com/watch?v=OKcrLfR-8mE&t=1s
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0:-1}  # Mapping remainders to the indices
        total = 0

        for i,num in enumerate(nums):
            total += num
            remainder = total % k
            if(remainder not in rem):
                rem[remainder] = i
            elif i - rem[remainder] > 1:
                return True
        return False