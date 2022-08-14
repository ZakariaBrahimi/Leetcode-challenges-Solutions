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
            res = (search(row+1, col, wordIndex+1) or
                   search(row-1, col, wordIndex+1) or
                   search(row, col+1, wordIndex+1) or
                   search(row, col-1, wordIndex+1))
            path.remove((row, col))
            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if search(row, col, 0): # board[row][col] == word[0] and 
                    return True
        return False
        