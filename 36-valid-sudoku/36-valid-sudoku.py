class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Declaring variables
        ROWS = len(board)
        COLS = len(board[0])
        valid = set()
        
        # 1. Check the validation of all rows -> by fixing the row number and move the col number
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in valid:
                    return False
                else:
                    valid.add(board[row][col])
            valid = set()
            
        # 2. Check the validation of all collumns -> by fixing the col number and move the row number
        for row in range(ROWS):
            for col in range(COLS):
                if board[col][row] == '.':
                    continue
                elif board[col][row] in valid:
                    return False
                else:
                    valid.add(board[col][row])
            valid = set()
        
        # 3. Check the validation of all sub-boxes
        #      a. Creating the 9 sub-boxes map 
        #      b. Iterate through the board
        #           - If the cell value already in the sub-box -> return False immediately
        subBoxes = {}
        for i in range(3):
            for j in range(3):
                subBoxes[(i,j)] = set()
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == '.':
                    continue
                else:
                    row_area, col_area = (row//3, col//3)
                    if board[row][col] in subBoxes[(row_area,col_area)]:
                        print(subBoxes)
                        return False
                subBoxes[(row_area,col_area)].add(board[row][col])
        
        # Note: if one of the last 3 steps given a False -> immediately return False
        
        # 4. If the last 3 steps are passed without returning False -> return True
        return True