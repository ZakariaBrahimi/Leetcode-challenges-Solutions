class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = [-num for num in nums]
        heapq.heapify(min_heap)
        while k != 0:
            output = heapq.heappop(min_heap)
            k -= 1
        return -output