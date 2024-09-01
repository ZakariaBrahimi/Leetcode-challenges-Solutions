import collections
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        # Solved Using Heap Sorting Algorithm
        # Time  Complexity: O(nlogn)
        # Space Complexity: O(n)

        # Create the chars counter
        counter = collections.Counter(s)
        # Convert dictionary to a list of tuples, using negative frequency for max-heap simulation
        heap = [(-freq, char) for char, freq in counter.items()]
        # Initialize the max-heap
        heapq.heapify(heap)
        # Keep popping from the max-heap and append to the result array
        result = []
        while heap: # On(n)
            freq, char = heapq.heappop(heap) # O(n), the time of: pop + restructure the heap
            result.append(char * -freq)  # Multiply character by its frequency
        # Joining the result array of chars
        return ''.join(result)
