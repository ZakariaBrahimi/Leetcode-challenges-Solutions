class Solution(object):
    def arrangeCoins(self, n):
        left = 0
        right = n
        
        while left <= right:
            middle = (left + right) // 2
            current_value =middle * (middle + 1) // 2
            if current_value == n:
                return middle
            elif n < current_value:
                right = middle - 1
            else:
                left = middle + 1
                
        return right
            