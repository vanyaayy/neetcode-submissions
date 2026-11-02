class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlocks = {i:[] for i in range(numCourses)}
        ind = [0]*numCourses
        output =[]
        for crs, pre in prerequisites:
            unlocks[pre].append(crs)
            ind[crs]+=1
        q = deque()
        for i in range(len(ind)):
            if ind[i]==0:
                q.append(i)
        while q:
            crs = q.popleft()
            output.append(crs)
            for p in unlocks[crs]:
                ind[p]-=1
                if ind[p]==0:
                    q.append(p)
        return output if len(output)==numCourses else []
