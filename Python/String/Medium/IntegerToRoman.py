'''
Link: https://leetcode.com/problems/integer-to-roman/
Time Complexity : O(n)
LeetCode Problem: 12. Integer to Roman
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        symlist = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),   ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

        res = []

        for sym, val in symlist:
            if num // val:
                count = num // val
                res.append(sym * count)
                num = num - val*count
        
        return ''.join(res)
        