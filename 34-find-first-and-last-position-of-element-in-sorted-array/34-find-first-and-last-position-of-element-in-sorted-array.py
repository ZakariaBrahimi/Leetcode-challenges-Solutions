class Solution(object):
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x > A[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x >= A[mid]: left = mid + 1
                else: right = mid - 1
            return right
        
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]
    
    
    """def searchRange(self, nums, target):
 
        
        left = 0
        right = len(nums) - 1
        result = []
        first_position = float('inf')
        last_position = float('-inf')
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                while nums[middle] == target:
                    middle += 1
                
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
                
        
        
        return [-1,-1]"""