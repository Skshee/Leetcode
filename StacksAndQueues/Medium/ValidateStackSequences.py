'''
Link : https://leetcode.com/problems/validate-stack-sequences/
Time Complexity : O(n)
Space Complexity : O(n)
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l = 0

        for val in pushed:
            stack.append(val)
            
            while len(stack) > 0 and stack[-1] == popped[l]:
                stack.pop()
                l += 1
        return len(stack) == 0