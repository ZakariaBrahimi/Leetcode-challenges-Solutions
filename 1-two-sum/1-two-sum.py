class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        hashMap = {}
        for index, num in enumerate(nums, start=0):
                RequiredVal = target - num
                if RequiredVal in hashMap:
                        return [hashMap[RequiredVal], index]
                hashMap[num] = index
        # Here I assume that we are going to return an empty array if we couldn't find the solution
        return [] 
