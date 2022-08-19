class Solution(object):
    def orangesRotting(self, grid):
        # Time Complexity : O(m*n)
        # Space Complexity: O(m*n)
        # BFS -> multy sources algorithm
        
        if not grid or not grid[0]: return 0
        directions   = [(0,1), (0,-1), (1,0), (-1,0)]
        fresh_orange = 0
        queue = []
        minutes  = 0
        ROWS  = len(grid)
        COLS  = len(grid[0])
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_orange += 1
                if grid[row][col] == 2:
                    queue.insert(0, (row, col))         
                    
        while fresh_orange > 0 and queue:
            length = len(queue)
            for _ in range(length):
                current_row, current_col = queue.pop()
                for row_direction, col_direction in directions:
                    new_row = current_row + row_direction
                    new_col = current_col + col_direction
                    if (0<=new_row<ROWS and 0<=new_col<COLS and
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh_orange -= 1
                        queue.insert(0, (new_row, new_col))
                        
            minutes += 1
        
        return minutes if fresh_orange == 0 else -1