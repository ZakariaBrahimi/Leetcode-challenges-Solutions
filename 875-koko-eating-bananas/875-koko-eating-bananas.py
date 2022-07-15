class Solution(object):
    def totalHours(self, middle, piles):
        """
        Returning The total number of hours to eat all bananas.
        """
        result = 0
        for banana in piles:
            result += ((banana-1)//middle) + 1
        
        return result
    
    def minEatingSpeed(self, piles, h):
        result = 0
        left = 1
        right = max(piles)
        
        while left <= right:
            middle = (left + right) // 2
            if self.totalHours(middle, piles) <= h:
                result = middle
                right = middle - 1
            else:
                left = middle + 1
            
        
        
        
        return result