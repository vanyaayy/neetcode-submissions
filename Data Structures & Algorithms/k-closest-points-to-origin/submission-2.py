class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        res=[]
        for x,y in points:
            heapq.heappush(minheap, (-(x**2+y**2),x,y))
            if len(minheap)>k:
                heapq.heappop(minheap)
        for d,x,y in minheap:
            res.append([x,y])

        return res
            
        

        