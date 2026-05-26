class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        stack.append('/')
        for p in path:
            if (not p or p == '.'):
                continue
            elif (len(stack)>=2 and p == '..'):
                stack.pop()
                stack.pop()
            elif (len(stack)==1 and p == '..'):
                continue
            elif(p == '/'):
                stack.append(p)
            else:
                stack.append(p)
                stack.append('/')
        # print(stack)
        string = ''.join(stack)
        if(len(string)>1):
            return string[:-1]
        else:
            return string