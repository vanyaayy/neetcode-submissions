class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append([r,c])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        count = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if (row<0 or row==len(grid) or col<0 or col==len(grid[0]) or grid[row][col]!=2**31-1):
                        continue
                    grid[row][col]=count
                    q.append([row,col])
            count+=1

                

            

    
        