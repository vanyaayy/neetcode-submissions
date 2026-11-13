class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        visit= set()
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if hashmap[crs]==[]:
                return True
            visit.add(crs)
            for p in hashmap[crs]:
                if not dfs(p):
                    return False
            hashmap[crs]=[]
            visit.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
