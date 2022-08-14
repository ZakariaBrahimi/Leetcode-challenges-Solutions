class Solution(object):
    def subsetsWithDup(self, nums):
        result = []
        subset = []
        nums.sort()
        
        def backtrack(index):
            if index == len(nums):
                result.append(subset[::]) # Appending the copy of subset not the original
                return 
            # All subsets that include nums[i]
            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()
            # All subsets that don't include nums[i]
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1)
            return
        
        backtrack(0)
        return result