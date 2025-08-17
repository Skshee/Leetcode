'''
Link : https://leetcode.com/problems/numbers-with-same-consecutive-differences/
Concept : Backtracking and DFS
'''

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        def dfs(N, num):
            if N == 0:
                ans.append(num)
                return
            last_digit = num % 10

            # set() avoids duplicate branches when k == 0
            # Ex - If k > 0, these are two different numbers most of the time (say last_digit = 7, k = 2 → (9, 5)).
            # But if k == 0, then both are the same (e.g. last_digit = 7 → (7, 7)) duplicate
            new_digits = {last_digit + k, last_digit - k}

            for new_digit in new_digits:
                if 0 <= new_digit < 10:
                    new_num = num * 10 + new_digit
                    dfs(N-1, new_num)

        for i in range(1,10):
            dfs(n-1,i)
        return ans
        