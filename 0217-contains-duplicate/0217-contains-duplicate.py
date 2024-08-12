class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brut Force Solution
        # Time Complexity : O(n2)
        # Space Complexity: O(1)

        # for index1 in range(len(nums)):
        #     for index2 in range(index1+1, len(nums)):
        #         if nums[index1] == nums[index2]:
        #             return True
        # return False

        # Optimal Solution
        # Time Complexity : O(n)
        # Space Complexity: O(n)

        hash_set = set()
        for number in nums:
            if number in hash_set:
                return True
            hash_set.add(number)
        return False
