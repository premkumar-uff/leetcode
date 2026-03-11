class Solution(object):
    def solveNQueens(self, n):
        board = [["."]*n for _ in range(n)]
        res = []      
        left = [0]*n
        upper = [0]*(2*n-1)
        lower = [0]*(2*n-1)
        self.solve(0, res, board, left, upper, lower, n)
        return res
    def solve(self, j, res, board, left, upper, lower, n):
        if j == n:
            temp = []
            for j in board:
                temp.append("".join(j))
            res.append(temp)
            return        
        for i in range(n):
            if left[i] == 0 and lower[i+j] == 0 and upper[n-1+j-i] == 0:                
                board[i][j] = "Q"
                left[i] = 1
                lower[i+j] = 1
                upper[n-1+j-i] = 1
                self.solve(j+1, res, board, left, upper, lower, n)
                board[i][j] = "."
                left[i] = 0
                lower[i+j] = 0
                upper[n-1+j-i] = 0
