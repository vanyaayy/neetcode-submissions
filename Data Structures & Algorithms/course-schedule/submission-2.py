class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i:[] for i in range(numCourses)}
        for crs, pr in prerequisites:
            pre[crs].append(pr)
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return False
            if pre[crs]==[]:
                return True
            visit.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            visit.remove(crs)
            pre[p]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
        

        