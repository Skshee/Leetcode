'''
Link : https://leetcode.com/problems/remove-duplicate-letters/
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Solving by using monotonically increasing stack
        last_occurence = {} # Stores the last occurence of every character in the dictionary
        stack = []

        for i,char in enumerate(s):
            last_occurence[char] = i
        
        for i in range(len(s)):
            # If character already in stack, then skip 
            if s[i] in stack:
                continue
            
            # Maintaining monotonic stack property but if we have reached last occurence index of a char then we let it be instead of popping it
            while stack and ord(stack[-1]) > ord(s[i]) and i < last_occurence[stack[-1]]:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)
            
