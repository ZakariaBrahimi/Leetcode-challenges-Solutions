class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        # We can either start from the step with index 0, or the step with index 1.
        return min(cost[0], cost[1])
            