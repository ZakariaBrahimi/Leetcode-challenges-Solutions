class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        # Time: O(n2) + O(n+m)
        [[1]]
        
        """
        """# Time Complexity : O(n*m)
        # Space Complexity: O(1)
        hasVisited = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def setToZeros(row, col):
            # row to zeros
            for r in range(ROWS):
                if matrix[r][col] == 0: # if already zero
                    continue
                matrix[r][col] = 0
                hasVisited.add((r, col))
            
            # col to zeros
            for c in range(COLS):
                if matrix[row][c] ==0:
                    continue
                matrix[row][c] = 0
                hasVisited.add((row, c))
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in hasVisited and matrix[row][col] == 0:
                    hasVisited.add((row, col))
                    setToZeros(row, col)
        
        return matrix"""
        
        # Time Complexity : O(n*m)
        # Space Complexity: O(1)
        zeroCells = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def setToZeros(row, col):
            # row to zeros
            for r in range(ROWS):
                matrix[r][col] = 0
            
            # col to zeros
            for c in range(COLS):
                matrix[row][c] = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    zeroCells.add((row, col))
        
        for row, col in zeroCells:
            setToZeros(row, col)
        
        return matrix
        
        
        
        
        
        
        
        
        
        
        
        
        
        