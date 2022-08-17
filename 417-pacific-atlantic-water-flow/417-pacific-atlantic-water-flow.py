class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]: return []
        rows     = len(heights)
        cols     = len(heights[0])
        pacific  = []
        atlantic = []
        pacific_visited  = set()
        atlantic_visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)] # 4 directions
        
        # Starting
        for col in range(cols):
            pacific.append((0, col))
            atlantic.append((rows-1, col))
        for row in range(rows):
            pacific.append((row, 0))
            atlantic.append((row, cols-1))
        
        
        def dfs(row, col, visitedOcean):
            # base case: visted
            if (row, col) in visitedOcean:
                return
            visitedOcean.add((row, col))
            for rowDirection, colDirection in directions:
                new_row = rowDirection + row
                new_col = colDirection + col
                if ( new_row >= 0  and new_row < rows and  new_col >= 0 and new_col < cols and 
                   ( new_row, new_col) not in visitedOcean and heights[new_row][new_col] >= heights[row][col]):
                    dfs(new_row, new_col, visitedOcean)
                
        
        
        for row, col in pacific:  dfs(row, col, pacific_visited)
        for row, col in atlantic: dfs(row, col, atlantic_visited)
        
        return pacific_visited & atlantic_visited # Intersection between 2 sets, (and ==> &&)
        