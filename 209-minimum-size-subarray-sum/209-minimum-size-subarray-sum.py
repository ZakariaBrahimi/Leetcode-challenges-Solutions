class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        
        target = 7
        nums = [2,3,1,2,4,3]
                          l
                          r
        """
        left = 0
        result = sys.maxsize # 2
        current_sum = 0 # 2+3+1+2=8-2=6+4=10-3=7-1=6+3=9-2=7-4=3
        result_value_has_changed = False
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                result = min(result, right-left+1)
                result_value_has_changed = True
                current_sum -= nums[left]
                left += 1
        if result_value_has_changed == False:
            return 0
        return result
            