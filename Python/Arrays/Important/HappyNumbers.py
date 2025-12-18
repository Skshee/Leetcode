'''
IMP Question : Asked often in Google Interviews
Link : https://leetcode.com/problems/happy-number/description/
Topic : Hashing, Math
Time Complexity : O(log n) where n is the number of digits in the number
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = str(n)

        while curr not in seen:
            seen.add(curr)
            summ = 0
            for digit in curr:
                summ += int(digit) ** 2
            if summ == 1:
                return True
            else:
                curr = str(summ)
        return False
