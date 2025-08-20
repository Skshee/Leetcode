'''
Link : https://leetcode.com/problems/numbers-with-same-consecutive-differences/
'''

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def backtrack(i, curr):
            if i == n:
                ans.append(curr)
                return 
            
            N = curr % 10
            
            vals = {N - k, N + k}
            
            for val in vals:
                if val >= 0 and val < 10:
                    new_num = curr*10 + val
                    backtrack(i+1, new_num)
        
        for i in range(1,10):
            backtrack(1,i)
        return ans