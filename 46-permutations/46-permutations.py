class Solution(object):
    def permute(self, nums):
        def dfs(nums, permutation):
            if len(nums) == 0:
                result.append(permutation)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], permutation+[nums[i]])
        
        result = list()
        dfs(nums, [])
        return result
        