class Solution(object):
    def climbStairs(self, n):
        steps = []
        memo = {}
        
        def memoization(n):
            if n in memo: return memo[n]
            if n == 0: return 1
            if n < 0 : return 0
            
            memo[n] = memoization(n-1) + memoization(n-2)
            return memo[n]
        
        memoization(n)
        return memoization(n)