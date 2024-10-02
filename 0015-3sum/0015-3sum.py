class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solved using Two Pointer Technique to avoid using three nested loops which means O(n3)
        # Time  Complexity: O(n²)
        # Space Complexity: O(n)

        # Sorting the Array: O(nlog(n))
        nums.sort()
        result = []

        # Looping + Two pointer 
        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                three_sum = nums[i] + nums[start] + nums[end]
                if three_sum == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif three_sum < 0:
                    start += 1
                else:
                    end -= 1

        # turn the arrays to tuples
        hashSet = set()
        for arr in result:
           hashSet.add(tuple(arr))

        # turn it out to array format
        res = []
        for tupl in hashSet:
           res.append(list(tupl))
        return res
        