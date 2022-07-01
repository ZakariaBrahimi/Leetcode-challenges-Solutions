class Solution(object):
    def reverse(self, nums, start, end):
        start = start
        end = end
        temp = 0
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, start=0, end=k-1)
        self.reverse(nums, start=k, end=len(nums)-1)
        return nums
        