class Solution(object):
    def threeSum(self, nums):
        result = []
        if len(nums) < 3:return []
        nums.sort()
        for i, a in enumerate(nums):
            if i> 0 and a == nums[i-1]: continue
            pointer1 = i+1
            pointer2 = len(nums)-1
            while pointer1 < pointer2:
                threeSum = a + nums[pointer1] + nums[pointer2]
                if threeSum > 0:
                    pointer2 -= 1
                elif threeSum < 0:
                    pointer1 += 1
                else:
                    result.append([a, nums[pointer1], nums[pointer2]])
                    pointer1 += 1
                    while pointer1 < pointer2 and nums[pointer1] == nums[pointer1 - 1]:
                        pointer1 += 1
       
        return result
                
        