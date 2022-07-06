class Solution(object):
    def minSubArrayLen(self, target, nums):

        left = 0
        result = sys.maxsize
        current_sum = 0 
        
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                result = min(result, right-left+1)
                current_sum -= nums[left]
                left += 1
        
        return result if result != sys.maxsize else 0
            