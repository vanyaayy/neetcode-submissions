class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res=[]
        for x,y in points:
            dist = x**2+y**2
            heapq.heappush(minheap, (dist,x,y))

        while minheap and len(res)!=k:
            d,x,y = heapq.heappop(minheap)
            res.append([x,y])
        
        return res


        