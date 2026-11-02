class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i:[] for i in range(numCourses)}
        visit = set()
        for crs, p in prerequisites:
            pre[crs].append(p)

        def dfs(crs):
            if pre[crs]==[]:
                return True
            if crs in visit:
                return False
            
            visit.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            pre[crs]=[]
            visit.remove(crs)
            return True
        
        for crs in pre:
            if not dfs(crs):
                return False
        return True
        