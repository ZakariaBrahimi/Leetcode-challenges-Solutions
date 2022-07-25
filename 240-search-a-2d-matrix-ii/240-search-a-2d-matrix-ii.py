class Solution(object):
    def searchMatrix(self, matrix, target):
        # set a pointer to the last element on the first row matrix[0][-1]
        # gain values ==>> top to the bottom (col) | Lose values ===>> right to left (row)
        # col = -1 | row = 0
        # if I need to lose values ===>> go to the left side means: (col - 1)
        # if II need to gain values ===>> go to the bottom means: (row + 1)
        
        # while (row < matrix.length and col >= -matrix[0].length)
        # if pointer == target: return true
        # if pointer < target: row + 1
        # if pointer > target: col - 1
        # returning False if the loop broked
        
        # Time Copmlexity: O(n+m), where n is number of rows - and m is the number of columns
        # Space Complexity: O(1)
        
        
        col = -1
        row = 0
        # here, I have added (-) to len(matrix[0]), cuz of (col >= -len(matrix[0]))
        while (row < len(matrix) and col >= -len(matrix[0])):
            pointer_val = matrix[row][col]
            if pointer_val == target: 
                return True
            elif pointer_val < target:
                row += 1
            else:
                col -= 1
        
        return False
        
        