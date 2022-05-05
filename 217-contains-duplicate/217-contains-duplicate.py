class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for num in nums:
                if num in hashSet:
                        return True
                hashSet.add(num)
        return False
        
