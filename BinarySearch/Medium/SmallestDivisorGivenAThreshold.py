'''
Link : https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
Complexity: O(n log(max(nums)))
'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if threshold < len(nums):
            return -1
        
        def check(divisor):
            Sum = 0
            for num in nums:
                Sum += ceil(num / divisor)
            return Sum <= threshold

        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right)//2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left        
        