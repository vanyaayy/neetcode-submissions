class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        minheap,res = [],[]
        c, time = 0,tasks[0][0]
        while minheap or c<len(tasks):
            while c<len(tasks) and time>=tasks[c][0]:
                heapq.heappush(minheap, (tasks[c][1], tasks[c][2]))
                c+=1
            if not minheap:
                time = tasks[c][0]
            else:
                p, ind = heapq.heappop(minheap)
                time+=p
                res.append(ind)
        return res
            




        