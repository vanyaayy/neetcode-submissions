class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area =0
        q =deque()
        def dfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            arr =1
            while q:
                directions = [[0,1],[1,0],[0,-1],[-1,0]]
                r,c = q.popleft()
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col]==1 and (row,col) not in visit:
                        arr+=1
                        visit.add((row,col))
                        q.append((row,col))
            return arr

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area = max(area, dfs(r,c))
        return area

        