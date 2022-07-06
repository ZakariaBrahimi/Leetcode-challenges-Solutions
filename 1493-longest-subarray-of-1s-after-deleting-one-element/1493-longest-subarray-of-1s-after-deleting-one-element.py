class Solution(object):
    def longestSubarray(self, nums):
        """
        must delete one item 
        
        [0,1,1,1,0,1,1,0,1]
        
        
        """
        result = 0
        left = 0
        ziro_counter = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                ziro_counter += 1
            while ziro_counter > 1:
                if nums[left] == 0:
                    ziro_counter -= 1
                left += 1
            result = max(result, right - left)
            
        return result