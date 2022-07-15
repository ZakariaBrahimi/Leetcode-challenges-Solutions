class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        1
        3

        """    
        m = len(matrix[0]) # number of columns = 1
        n = len(matrix) # number of rows = 2
        left = 0 # 1
        right = (n*m)-1 # = 1
        
        while left <= right:
            mid = (left+right)/2 # = 1
            # the value of that mid index
            row = mid/m # = 0
            col = mid%m # = 1
            #if row > len(matrix)-1 or col > len(matrix[0])-1:break
            if matrix[row][col] == target: # = 1
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        