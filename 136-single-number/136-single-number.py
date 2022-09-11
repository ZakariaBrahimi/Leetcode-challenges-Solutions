class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        [4,1,2,1,2]
        [5123321]
        {5,1,2,3}
        
        1. Initializeing empty hash set
        
        2. Loop throught the array
            -> if nums[i] in set:
                -> remove nums[i] from the set
                
            -> if nums[i] not in set:
                -> set.add(nums[i])
        
        """
        
        hashSet = set()
        for num in nums:
            if num in hashSet:
                hashSet.remove(num)
            else:
                hashSet.add(num)
        
        return hashSet.pop()