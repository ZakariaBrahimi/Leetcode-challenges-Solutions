class Solution(object):
    def exist(self, board, word):
        path = set()
        def search(row, col, wordIndex):
            if wordIndex == len(word): 
                return True
            
            if (row < 0 or col < 0 or 
                row >= len(board) or col >= len(board[0]) or
                board[row][col] != word[wordIndex] or
                (row, col) in path):
                return False
            
            path.add((row, col))
            result = (search(row+1, col, wordIndex+1) or
                   search(row-1, col, wordIndex+1) or
                   search(row, col+1, wordIndex+1) or
                   search(row, col-1, wordIndex+1))
            path.remove((row, col))
            return result
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if search(row, col, 0): # board[row][col] == word[0] and 
                    return True
        return False
    # Time Complexity: O(n * m * 4^n), 
    # where 4 is the number of recursive calls (on result variable)
        