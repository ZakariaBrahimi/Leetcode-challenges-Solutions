class Solution(object):
    def minCostClimbingStairs(self, cost):
        def solve(steps):
            if steps in memo: return memo[steps]
            if steps == 0: return cost[0]
            if steps == 1: return cost[1]
            
            memo[steps] = cost[steps] + min(solve(steps-1), solve(steps-2))
            return memo[steps]
        memo = dict()
        steps = len(cost)
        return min(solve(steps-1), solve(steps-2))
        
        
        # Using bottom-up (tabulation) approach
        """
        cost.append(0) # the cost of setting on the top of the floor is 0
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        # We can either start from the step with index 0, or the step with index 1.
        return min(cost[0], cost[1])"""
            