class Solution(object):
    def leastInterval(self, tasks, n):
        # Solving the problem by figuring out the pattern
        # This Approach is more optimal solution than th Max Heap && Queue Approach
        # Time Complexity: O(n) in worst case
        # Space Complexity: O(n)
        count = collections.Counter(tasks) # {letter:occurence}
        freq = [val for val in count.values()]
        max_freq = max(freq)
        max_freq_tasks = freq.count(max_freq)
        
        return max(len(tasks), (max_freq - 1) * (n + 1) +  max_freq_tasks)
        
        
        # Max Heap && Queue Approach
        # Time Complexity: 
        # Space Complexity: 
        """
        def leastInterval(self, tasks, n):
            time_required = 0
            count         = collections.Counter(tasks) # {letter:occurence}
            queue         = []
            max_heap      = [-val for val in count.values()]
            heapq.heapify(max_heap) 
        
            while max_heap or queue:
                time_required += 1
                if max_heap:
                    current_task  = 1 + heapq.heappop(max_heap)
                    if current_task:
                        rest = time_required + n # 12
                        queue.insert(0, [current_task, rest])
                if queue and queue[-1][1] == time_required:
                    val = queue.pop()[0] # 0
                    heapq.heappush(max_heap, val)
            
            return time_required
        """
            
        
        