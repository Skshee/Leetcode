'''
Link : https://leetcode.com/problems/combination-sum-iii/ 
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(start: int, curr: List[int], curSum: int):
            if len(curr) == k:
                if curSum == n:
                    ans.append(curr[:])
                return

            for j in range(start, 10):
                if curSum + j > n:
                    break
                curr.append(j)
                backtrack(j + 1, curr, curSum + j)
                curr.pop()

        backtrack(1, [], 0)
        return ans
