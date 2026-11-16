class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col = len(grid), len(grid[0])
        visit = set()
        count=0
        def dfs(r,c):
            if r in range(row) and c in range(col) and (r,c) not in visit and grid[r][c]=="1":
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1" and (r,c) not in visit:
                    count+=1
                    dfs(r,c)
                    
        return count
            

        