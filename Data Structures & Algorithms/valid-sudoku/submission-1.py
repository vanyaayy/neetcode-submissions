class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] in rows[i] or board[j][i] in cols[i]:
                    return False
                if board[i][j]!=".":
                    rows[i].append(board[i][j])
                if board[j][i]!=".":
                    cols[i].append(board[j][i])
        for i in range(9):
            for j in range(9):
                if board[i][j] in squares[(i//3, j//3)]:
                    return False
                if board[i][j]!=".":
                    squares[(i//3, j//3)].append(board[i][j])
        return True
                

                
        