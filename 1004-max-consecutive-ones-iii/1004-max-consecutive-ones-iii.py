class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        result = 0
        zero_counter = 0
        while (right < len(nums)):
            if nums[right] == 0:
                zero_counter += 1
            
            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1
            result = max(result, right-left+1)
            right += 1
         
        return result      
        