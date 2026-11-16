class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minheap = []
        res=[]
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key =lambda t: t[0])
        time = tasks[0][0]
        i=0
        while minheap or i<len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(minheap, (tasks[i][1], tasks[i][2]))
                i+=1
            if minheap:
                proc, index = heapq.heappop(minheap)
                time+=proc
                res.append(index)
            else:
                time=tasks[i][0]
        return res



       



        


            