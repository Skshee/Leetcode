'''
Link : https://leetcode.com/problems/add-binary/description/?envType=problem-list-v2&envId=bit-manipulation
'''

# Case 1 - Without using binary wala library

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length_a = len(a)
        length_b = len(b)
        num1 = 0
        num2 = 0
        res = ''

        for i,digit in enumerate(a):
            digit = int(digit)
            num1 += digit*(2**(length_a - i - 1))
        print(num1)

        for i,digit in enumerate(b):
            digit = int(digit)
            num2 += digit*(2**(length_b - i - 1))
        print(num2)  

        Sum = num1 + num2

        if(Sum == 0):
            return "0"

        while Sum > 0:
            rem = Sum % 2
            res += str(rem)
            Sum = Sum // 2
        res = res[::-1]
        return res
