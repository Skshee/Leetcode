'''
Link : https://leetcode.com/problems/combination-sum/
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, curr = [], []
        n = len(candidates)

        def backtrack(i, curSum):
            if curSum == target:
                ans.append(curr[:])
                return

            if curSum > target or i == n:
                return

            backtrack(i+1, curSum)

            curr.append(candidates[i])
            backtrack(i, curSum + candidates[i])
            curr.pop()

        backtrack(0,0)
        return ans