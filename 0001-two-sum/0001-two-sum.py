class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     j = i+1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         j += 1
        
        hashTable = dict() # {nums[i]: index}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = i
        print(hashTable)
        for i in range(len(nums)):
            numberToSearch = target - nums[i]
            if numberToSearch in hashTable and hashTable[numberToSearch] != i:
                return [i, hashTable[numberToSearch]]


        """
        nums = [2,11,8,7], target = 9
        setOf6 = {2, 11}

        for number in nums:
            if number not in setOf6:
                if sum(setOf6) == target:
                    return [index of 1, and 2]

                if sum(setOf6) < target:


                if sum(setOf6) > target:




        """
        # for 