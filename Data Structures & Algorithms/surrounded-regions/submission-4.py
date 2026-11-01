class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # visit = set()
        def dfs(r,c):
            if r in range(rows) and c in range(cols) and board[r][c]=="O":
                board[r][c]="T"
                # visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r, c-1)
        

        for r in range(rows):
            for c in range(cols):
                if (r==0 or r==rows-1 or c==0 or c==cols-1) and board[r][c]=="O":
                    dfs(r,c)
     
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
