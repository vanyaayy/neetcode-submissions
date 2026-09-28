class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        dist = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if (row>=0 and row<rows and col>=0 
                    and col<cols and grid[row][col]==2**31-1):
                        grid[row][col] = dist
                        q.append((row,col))
            dist+=1
    




        