class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
         # [1,1,0,1,1,1] , len = 6
            
        right = 0 # 
        count = 0 # 
        result = 0 # 
        
        while right < len(nums):
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
        