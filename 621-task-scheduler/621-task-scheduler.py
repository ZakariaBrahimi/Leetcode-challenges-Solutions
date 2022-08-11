class Solution(object):
    def leastInterval(self, tasks, n):
        count = collections.Counter(tasks) # {letter:occurence}
        freq = [val for val in count.values()]
        max_freq = max(freq)
        max_freq_tasks = freq.count(max_freq)
        
        return max(len(tasks), (max_freq - 1) * (n + 1) +  max_freq_tasks)
        
        
        
        """
        def leastInterval(self, tasks, n):
        count = collections.Counter(tasks) # {letter:occurence}
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap) # [], n = 2
        time_required = 0 # 12
        queue = [] # [ [1,12]  ]
        
        while max_heap or queue:
            time_required += 1
            if max_heap:
                current_task  = 1 + heapq.heappop(max_heap) # 1
                if current_task:
                    rest = time_required + n # 12
                    queue.insert(0, [current_task, rest])
            if queue and queue[-1][1] == time_required:
                val = queue.pop()[0] # 0
                heapq.heappush(max_heap, val)
            
        return time_required
        """
            
        
        