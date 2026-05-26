'''
Link : https://leetcode.com/problems/reverse-integer/?envType=problem-list-v2&envId=math

IMP CONSTRAINT : If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0
'''

class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        Sum = 0
        while num > 0:
            rem = num % 10
            Sum = Sum*10 + rem
            num = num // 10
        if(Sum > 2**31-1):
            return 0
        elif(x < 0):
            Sum *= -1
        return Sum



