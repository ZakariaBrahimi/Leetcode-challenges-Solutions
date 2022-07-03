class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            result.append(prod)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:continue
            prod *= nums[i+1]
            result[i] = result[i]*prod
        return result