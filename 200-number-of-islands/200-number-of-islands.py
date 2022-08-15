class Solution(object):
    def numIslands(self, grid):
        def dfs(row, col):
            stack = [(row, col)]
            
            while stack:
                current_row, current_col = stack.pop()
                if not (current_row < 0 or current_row >= rows or
                    current_col < 0 or current_col >= cols or
                    grid[current_row][current_col] == "0"  or
                    (current_row, current_col) in visited):
                    
                    visited.add((current_row, current_col))
                    
                    
                    stack.append((current_row-1, current_col))
                    stack.append((current_row+1, current_col))
                    stack.append((current_row,   current_col-1))
                    stack.append((current_row, current_col+1))
            
            
            """dfs(row-1, col) # top direction
            dfs(row+1, col) # down direction
            dfs(row, col+1) # right direction
            dfs(row, col-1) # left direction"""
            
        if not grid: return 0
        visited = set()
        islands_counter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    islands_counter += 1

        return islands_counter
    
    
    
    
    """def numIslands(self, grid):
        def dfs(row, col):
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] == "0"  or
                (row, col) in visited):
                return

            visited.add((row, col))
            dfs(row-1, col) # top direction
            dfs(row+1, col) # down direction
            dfs(row, col+1) # right direction
            dfs(row, col-1) # left direction
            
        if not grid: return 0
        visited = set()
        islands_counter = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    islands_counter += 1

        return islands_counter"""