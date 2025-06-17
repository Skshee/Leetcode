class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(','}':'{',']':'['}
        stack = []

        for char in s:
            if(char in dic.values()):
                stack.append(char)
            elif(char in dic.keys()):
                if(not stack or dic[char] != stack[-1]):
                    return False
                else:
                    stack.pop()
        if(len(stack)==0):
            return True
        else:
            return False
                