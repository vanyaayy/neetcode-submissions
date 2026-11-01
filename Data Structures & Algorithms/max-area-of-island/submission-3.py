class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0
        def dfs(r,c):
            if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visit:
                visit.add((r,c))
                return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1)+dfs(r,c+1))
            else:
                return 0
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    area = max(area, dfs(r,c))
        return area
     

        