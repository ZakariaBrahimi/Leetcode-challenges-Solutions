class Solution(object):
    def findMaxConsecutiveOnes(self, nums):          
        count = 0 
        result = 0       
        
        for right in range(len(nums)):
            if nums[right] == 0 :
                result = max(result, count)
                right = right + 1
                count = 0
            else:
                count += 1
                right += 1
            
            if right == len(nums):
                result = max(result, count)
                
        return result
        