class KthLargest(object):

    def __init__(self, k, nums):
        self.minHeap = nums # [[4, 5, 8, 2]]
        self.k    = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        

    def add(self, val):
        if len(self.minHeap) >= self.k:
            heapq.heappushpop(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
        
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)