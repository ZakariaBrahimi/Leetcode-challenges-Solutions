class Solution(object):
    def climbStairs(self, n):
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i  in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
        
        
        '''
        steps = []
        memo = {}
        
        def memoization(n):
            if n in memo: return memo[n]
            if n == 0: return 1
            if n < 0 : return 0
            
            memo[n] = memoization(n-1) + memoization(n-2)
            return memo[n]
        
        return memoization(n)
        '''
    

