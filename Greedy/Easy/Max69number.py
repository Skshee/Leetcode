'''
Link : https://leetcode.com/problems/maximum-69-number/
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        number_string = str(num)
        n = len(number_string)
        new_number = str(num)

        for i in range(n):
            if number_string[i] == '6':
                new_number = number_string[:i] + '9' + number_string[i+1:]
                break
        return int(new_number)
        