class Solution(object):
    def isPerfectSquare(self, num):
        """
        1,4,9, 16  25  36  49  64  81  100  110
        1,2,3, 4,  5,  6,  7,  8,  9,  10,  11,  12,13,14,16
        l      m               r                          
        
        """
        left = 1
        right = num
        
        while left <= right:
            middle = (left + right) // 2
            if middle*middle == num:
                return True
            elif middle*middle < num:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
        

        
        