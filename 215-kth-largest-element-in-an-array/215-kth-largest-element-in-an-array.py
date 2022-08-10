class Solution(object):
    
    def findKthLargest(self, nums, k):
        # Quick Select Approach
        k = len(nums) - k
        def quickSelect(left, right):
            pivot = nums[right]
            pointer = left
            
            for i in range(left, right):
                if pivot >= nums[i]:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            
            nums[pointer], nums[right] = pivot, nums[pointer]
            if pointer == k: return nums[pointer]
            elif pointer < k: return quickSelect(pointer+1, right)
            else: return quickSelect(left, pointer-1)
            
            
            
        return quickSelect(0, len(nums) - 1)
    
    
    
    # This is working solution using Heap Data Structure
    # Time Complexity: O(n), where n is the length of array
    # Space Complexity: O(1), No extra memory !
    """
    def findKthLargest(self, nums, k):
        min_heap = [-num for num in nums] # it's simulation to Max Heap
        heapq.heapify(min_heap)
        while k != 0:
            output = heapq.heappop(min_heap)
            k -= 1
        return -output
    """