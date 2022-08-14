class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        subset = []
        
        
        def backtrack(index):
            if target == sum(subset):
                result.append(subset[:])
                return
            if sum(subset) > target or index == len(candidates):
                return
            
            subset.append(candidates[index])
            backtrack(index+1)
            subset.pop()
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            backtrack(index+1)
            return
        
        backtrack(0)
        return result