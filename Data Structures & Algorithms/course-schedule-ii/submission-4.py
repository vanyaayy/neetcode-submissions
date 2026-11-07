class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        visit, cycle = set(), set()
        output=[]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return output

        
        