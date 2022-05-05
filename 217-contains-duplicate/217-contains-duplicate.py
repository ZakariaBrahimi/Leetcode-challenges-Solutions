class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashMap = {}
        for num in nums:
                if num in hashMap:
                        return True
                else:
                        hashMap[num] = 1
        return False
        