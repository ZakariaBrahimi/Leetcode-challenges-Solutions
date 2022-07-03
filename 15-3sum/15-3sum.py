class Solution(object):
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:return []
        nums.sort()
        for i, a in enumerate(nums):
            if i> 0 and a == nums[i-1]: continue
            start = i+1
            end = len(nums)-1
            while start < end:
                threeSum = a + nums[start] + nums[end]
                if threeSum > 0:
                    end -= 1
                elif threeSum < 0:
                    start += 1
                else:
                    result.append([a, nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
       
        return result
                
        