'''
Link : https://leetcode.com/problems/water-bottles/
Time Complexity : O(log n)
Space Complexity : O(1)
'''
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        remainingFull = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_bottles = empty // numExchange
            remainder = empty % numExchange
            total += new_bottles
            empty = new_bottles + remainder

        return total