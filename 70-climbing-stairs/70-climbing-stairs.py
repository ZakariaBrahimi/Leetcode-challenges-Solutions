class Solution(object):
    def climbStairs(self, n):
        # Using Tabulation(bottom-up) method
        one = 1
        two = 1
        for i in range(2, n+1):
            temp = one + two
            two = one
            one = temp
        return one
        # Using Tabulation(bottom-up) method, 
        # but here the space complexity is O(n)
        '''
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i  in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
        '''
        # Using Memoization(top-down) method
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
    

