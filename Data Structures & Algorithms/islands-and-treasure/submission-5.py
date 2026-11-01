class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        distance =1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            for i in range(len(q)):
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==2**31-1:
                        q.append((row,col))
                        grid[row][col] = distance
            distance+=1

        

        