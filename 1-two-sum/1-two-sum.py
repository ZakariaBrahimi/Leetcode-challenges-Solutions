class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        hashMap = {}
        if len(nums) == 2: return [0,1]
        for index, num in enumerate(nums, start=0):
                RequiredVal = target - num
                if RequiredVal in hashMap:
                        return [hashMap[RequiredVal], index]
                hashMap[num] = index
