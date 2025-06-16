'''
Link : https://leetcode.com/problems/multiply-strings/
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        sum1 = 0
        sum2 = 0


        for i,digit in enumerate(num1):
            digit = int(digit)
            sum1 = sum1 + digit*(10**(len1 - i - 1))
        print(sum1)

        for i,digit in enumerate(num2):
            digit = int(digit)
            sum2 = sum2 + digit*(10**(len2 - i - 1))
        print(sum2)

        return str(sum1 * sum2)
