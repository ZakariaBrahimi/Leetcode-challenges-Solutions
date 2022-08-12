class Solution(object):
    def subsets(self, nums):
        result = list()
        subarr = []
        def dfs(index):
            if index == len(nums):
                result.append(list(subarr))
                return
            
            subarr.append(nums[index])
            dfs(index+1)
            subarr.pop()
            dfs(index+1)
            return
        
        dfs(0)
        return result