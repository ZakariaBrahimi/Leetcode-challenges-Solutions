class Solution(object):
    def rob(self, nums):
        memo = {}
        def dynamicProgrammingSolution(i):
            if i in memo: return memo[i]
            if i >= len(nums): return 0
            
            option1 = nums[i] +  dynamicProgrammingSolution(i+2)
            option2 = dynamicProgrammingSolution(i+1)
            memo[i] = max(option1, option2)
            return memo[i]
        
        return dynamicProgrammingSolution(0)
        
        
        
        """if len(nums) == 2: return max(nums)
        result = [0]
        current_sum = [0]
        def dynamicProgrammingSolution(houseNumber):
            if houseNumber == len(nums)-2 or houseNumber == len(nums)-1: 
                result[0] = max(result[0], current_sum[0])
                return result[0]
            current_sum[0] += nums[houseNumber]
            for i in range(houseNumber+2, len(nums)):
                
                dynamicProgrammingSolution(i)
            current_sum[0] -= nums[i]
            
            return result[0]
        
        return max(dynamicProgrammingSolution(0), dynamicProgrammingSolution(1))"""