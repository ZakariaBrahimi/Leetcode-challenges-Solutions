class Solution(object):
    def kClosest(self, points, k):
        min_heap = [[math.sqrt(point[0]**2 + point[1]**2), point] for point in points]  
        heapq.heapify(min_heap)
        result = list()
        while k != 0:
            closest = heapq.heappop(min_heap)
            result.append(closest)
            k -= 1
        return [point[1] for point in result]