class Solution(object):
    def subsets(self, nums):
        result = list()
        subset = []
        def dfs(index):
            if index == len(nums):
                result.append(list(subset)) # Making a copy of the subset
                return
            
            subset.append(nums[index])
            dfs(index+1)
            subset.pop()
            dfs(index+1)
            return
        
        dfs(0)
        return result