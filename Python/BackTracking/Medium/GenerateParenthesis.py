'''
Link : https://leetcode.com/problems/generate-parentheses/
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(left, right, curr):
            if len(curr) == 2*n:
                ans.append(curr[:])
                return

            if left < n:
                backtrack(left + 1, right, curr + '(')

            if right < left:
                backtrack(left, right + 1, curr + ')')

        backtrack(0,0,"")
        return ans
        

        