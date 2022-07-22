class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r )//2
            
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] == target:
                return mid
        
        return -1