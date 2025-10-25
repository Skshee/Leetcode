'''
Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description
Time Complexity : O(n)
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        amount = [0] * n
        amount[0] = 1
        count = 1
        step = 0

        while count < n:
            if count % 7 != 0:
                amount[count] = amount[count - 1] + 1
                count += 1
            else:
                amount[count] = amount[count - 7] + 1
                count += 1
        return sum(amount)
        