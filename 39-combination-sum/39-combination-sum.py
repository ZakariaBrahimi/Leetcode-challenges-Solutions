class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        subset = []
        
        def dfs(index):
            if sum(subset) == target:
                result.append(subset[:]) # Append a copy not the original subset
                return
            if index == len(candidates) or sum(subset) > target:
                return
            
            subset.append(candidates[index])
            dfs(index)
            subset.pop()
            dfs(index+1)
            return
        
        dfs(0)
        return result 