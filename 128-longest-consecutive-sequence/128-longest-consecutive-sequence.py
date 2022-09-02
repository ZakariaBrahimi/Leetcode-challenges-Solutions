class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity : O(n)
        Space Complexity: O(n)
        
        Edge Case: if len[array] == 1: return 1
        
        1. Create a hash set to stor all elements on the given integer array
            -> for constant lookups
        
        2. Iterating other the given array
        
        3. if [current integer] + 1 in hashSet or [current integer] - 1 in hashSet: (tow separate while loops)
            -> result.append(current)
        
        4. Return len(result)
        
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        numsSet = {num for num in nums}
        lengest_sequence = 0
        current_sequence = 0
        
        for num in nums:
            if (num - 1) not in numsSet:
                current = num
                current_sequence = 1
                while (current+1) in numsSet:
                    current_sequence += 1
                    current = current + 1
                lengest_sequence = max(lengest_sequence, current_sequence)
            """current = num 
            while (current-1) in numsSet:
                result.append(current)
                current = current - 1"""

        return lengest_sequence