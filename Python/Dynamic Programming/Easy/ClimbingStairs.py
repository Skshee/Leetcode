'''
Link : https://leetcode.com/problems/climbing-stairs/
Actually refer all solutions given here : https://neetcode.io/problems/climbing-stairs/solution
and https://chatgpt.com/c/6a4f467b-4a80-83e8-b762-f7cd9e5c2609
'''
# DFS method
class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down Approach
        self.ways = 0
        def dfs(i):
            if i >= n:
                return i == n # 1 if equal, 0 if not
            return dfs(i+1) + dfs(i+2)
        
        return dfs(0)
    
#DP method(Memoization of dfs)
            



            
        