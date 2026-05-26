'''
Link : https://leetcode.com/problems/climbing-stairs/
'''
# Faster DP method
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i == 1 or i == 0:
                return 1
            
            if i in memo:
                return memo[i]

            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        
        memo = {}
        return dp(n)

# Slower recursion
    int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return climbStairs(n-1) + climbStairs(n-2);
    }
        