class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            # Check if stack is not empty and top element forms a "bad" pair with current char
            if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char) 
        
        return "".join(stack)