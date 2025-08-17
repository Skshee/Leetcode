'''
Link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        mappings = {
            '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'
        }

        ans, curr = [], []

        def backtrack(i):
            if i >= len(digits):
                ans.append(''.join(curr))
                return

            for char in mappings[digits[i]]:
                curr.append(char)
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        return ans