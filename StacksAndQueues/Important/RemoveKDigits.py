'''
Link : https://leetcode.com/problems/remove-k-digits/description/?envType=problem-list-v2&envId=monotonic-stack
Reference : https://www.youtube.com/watch?v=cFabMOnJaq0
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        pop_count = 0
        
        for digit in num:
            while stack and stack[-1] > digit and pop_count < k:
                stack.pop()
                pop_count += 1
            stack.append(digit)
        
        # Remove extra digits from end if k not yet reached
        while pop_count < k:
            stack.pop()
            pop_count += 1
        
        # Remove leading zeros
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        
        result = ''.join(stack[i:])
        if result:
            return result
        else: 
            return "0"
