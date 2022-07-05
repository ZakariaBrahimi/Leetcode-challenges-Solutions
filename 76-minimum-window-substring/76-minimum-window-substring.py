import collections
import sys

class Solution:
    def minWindow(self, searchString, t):
        '''
        :type searchString: str
        :type t: str
        :rtype: str
        '''
        left = 0
        right = 0
        
        # It stores the length of maximum valid substring 
        minimum = sys.maxsize
        counter_t = collections.Counter(t)
        counter_search = collections.defaultdict(int)
        count = 0
        minimum_window = ""

        # Here we use the 2 pointers approach
        while right < len(searchString):
            counter_search[searchString[right]] += 1
            if searchString[right] in counter_t: 
                if counter_search[searchString[right]] <= counter_t[searchString[right]]:
                    count += 1
            
            while left <= right and count == len(t):
                if minimum > right - left + 1:
                    minimum = right - left + 1
                    minimum_window = searchString[left : right + 1]
                
                counter_search[searchString[left]] -= 1
                if searchString[left] in counter_t and counter_search[searchString[left]] < counter_t[searchString[left]]:
                    count-=1
                    
                left += 1
            
            right += 1
            
        return minimum_window
