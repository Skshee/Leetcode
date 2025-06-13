class Solution:
    def isPalindrome(self, x: int) -> bool:
        Sum = 0
        num = x
        while x>0:
            rem = x % 10
            Sum = Sum * 10 + rem
            x = x//10
        if(Sum == num):
            return True
        else:
            return False