class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        dist = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        
        while q:
            for i in range(len(q)):
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if (row>=0 and row<rows and col>=0 
                    and col<cols and grid[row][col]>=1 
                    and (row, col) not in visit):
                        grid[row][col] = dist
                        q.append((row,col))
                        visit.add((row,col))
            dist+=1
    




        