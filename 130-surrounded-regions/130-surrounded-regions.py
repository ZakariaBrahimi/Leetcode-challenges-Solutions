class Solution(object):
    def solve(self, board):
        # Time Complexity : O(n*m)
        # Space Complexity: O(n*m)
        if not board or not board[0]: return []
        ROWS = len(board)
        COLS = len(board[0])
        hasVisited = set()
        
        def mark(row, col):
            # base cases: out of bounds & equal to 'X' & not visited
            if row<0 or row == ROWS or col<0 or col == COLS: return # out of bounds
            if board[row][col] == 'X': return
            if (row, col) in hasVisited: return
            
            hasVisited.add((row, col))
            board[row][col] = 1
            mark(row+1, col)
            mark(row-1, col)
            mark(row, col+1)
            mark(row, col-1)
        
        # 1. mark all unsurrounded  regions with 1
        # surrounded regiens are in border or adjacent to it.
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == 'O' and
                   (row, col) not in hasVisited and 
                   (row in [0, ROWS-1] or col in [0, COLS-1])):
                    mark(row, col)
        
        # 2. mark all remaining 'O' regions with 'X'
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != 1:
                    board[row][col] = 'X'
        # 3. mark all '1' regions with 'O'
                else:
                    board[row][col] = 'O'
        
        return board
    
    

    # Another similar approach
        """
        if not board or not board[0]: return []
        ROWS = len(board)
        COLS = len(board[0])
        hasVisited = set()
        unsurrounded_regions = set()
        
        def mark(row, col):
            # base cases: out of bounds & equal to 'X' & not visited
            if row<0 or row == ROWS or col<0 or col == COLS: return # Out of bounds
            if board[row][col] == 'X': return
            if (row, col) in hasVisited or (row, col) in unsurrounded_regions: return
            
            hasVisited.add((row, col))
            unsurrounded_regions.add((row, col))
            mark(row+1, col)
            mark(row-1, col)
            mark(row, col+1)
            mark(row, col-1)
        
        # 1. mark all unsurrounded  regions with 1
        # surrounded regiens are in border or adjacent to it.
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == 'O' and
                   (row, col) not in hasVisited and 
                   (row in [0, ROWS-1] or col in [0, COLS-1])):
                    mark(row, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in unsurrounded_regions:
                    board[row][col] = 'X'                
                    
        return board
        """