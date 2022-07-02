class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        prefix = [1]
        postfix = [1]
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            prefix.append(prod)
        prod = 1
        
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            postfix.insert(0, prod)
                
        for i in range(len(nums)):
            som = prefix[i]*postfix[i]
            result.append(som)
        return result
        