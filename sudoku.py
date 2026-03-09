class Solution(object):
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for c in "123456789":
                        if self.valid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            board[i][j] = "."
                    return False
        return True

    def valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                return False
        return True
