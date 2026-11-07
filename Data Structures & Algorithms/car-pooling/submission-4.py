class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        minheap =[]
        cur =0
        for t in trips:
            while minheap and t[1]>=minheap[0][0]:
                endT, pas = heapq.heappop(minheap)
                cur-=pas
            cur+=t[0]
            heapq.heappush(minheap, (t[2],t[0]))
            if cur>capacity:
                return False
        return True
            

        