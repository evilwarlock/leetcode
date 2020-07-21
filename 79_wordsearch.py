class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        row, col = len(board), len(board[0])
        
                    
        def dfs(idx, i, j, pos):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != word[idx]:
                return False
            pos = pos + 1
            tmp = board[i][j]
            board[i][j] = '*'
            if pos == len(word):
                return True
            if dfs(idx+1, i+1, j, pos):
                return True
            if dfs(idx+1, i-1, j, pos):
                return True
            if dfs(idx+1, i, j+1, pos):
                return True
            if dfs(idx+1, i, j-1, pos):
                return True
            board[i][j] = tmp
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, 0):
                        return True