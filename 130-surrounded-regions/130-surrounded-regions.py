class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return []
        rows = len(board)
        cols = len(board[0])
        hasVisited = set()
        
        def mark(row, col, markType):
            # base cases: out of bounds | equal to 'X'
            if row<0 or row == rows or col<0 or col == cols: return
            if board[row][col] == 'X': return
            if (row, col) in hasVisited: return
            
            hasVisited.add((row, col))
            board[row][col] = 1
            mark(row+1, col, 1)
            mark(row-1, col, 1)
            mark(row, col+1, 1)
            mark(row, col-1, 1)
        
        # 1. mark all wrong regions with 1
        # Wrong regiens are in border or adjacent to it
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row, col) not in hasVisited and (row in [0, rows-1] or col in [0, cols-1]):
                    mark(row, col, 1)
        
        # 2. mark all remaining regiens with 'X'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] != 1:
                    board[row][col] = 'X'
        
        # 3. mark all '1' to 'O'
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    board[row][col] = 'O'
        
        return board