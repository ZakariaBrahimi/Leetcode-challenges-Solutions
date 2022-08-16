class Solution(object):
    def maxAreaOfIsland(self, grid):
        max_area = 0
        current_area = [0]
        visited  = set()
        rows     = len(grid)
        cols     = len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0 or (row, col) in visited:
                return
            visited.add((row, col))
            current_area[0] += 1
            
            dfs(row+1, col) # down direction 
            dfs(row-1, col) # top direction
            dfs(row, col+1) # right direction
            dfs(row, col-1) # left direction
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                max_area      = max(max_area, current_area[0])
                current_area[0] = 0
        
        return max_area if grid else 0