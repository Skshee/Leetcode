'''
Link : https://leetcode.com/problems/koko-eating-bananas/
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k) # Higher integer value of float, eg : 3.2 becomes 4
            return hours <= h

        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right)//2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
