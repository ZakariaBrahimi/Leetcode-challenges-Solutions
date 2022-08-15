class Solution(object):
    def numIslands(self, grid):
        def dfs(row, col):
            if (row < 0 or row >= rows or col < 0 or col >= cols ):
                return
            
            
            if grid[row][col] == '1':
                grid[row][col] = 0   
                dfs(row-1, col)   # top direction
                dfs(row+1, col)   # down direction
                dfs(row,   col+1) # right direction
                dfs(row,   col-1) # left direction
            return
                
        if not grid: return 0
        visited = set()
        islands_counter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands_counter += 1
                    
        
        
        return islands_counter
                    