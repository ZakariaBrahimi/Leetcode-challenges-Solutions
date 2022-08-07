class Solution(object):
    def lastStoneWeight(self, stones):
        stones_min_heap = [-stone for stone in stones] # Python doesn't soppurt Min Heap
        heapq.heapify(stones_min_heap)
        
        while len(stones_min_heap) > 1:
            y = -(heapq.heappop(stones_min_heap))
            x = -(heapq.heappop(stones_min_heap))
            
            if x != y:
                rest = y - x
                heapq.heappush(stones_min_heap, -rest)
        
        return -stones_min_heap[0] if len(stones_min_heap) == 1 else 0
                
        
        