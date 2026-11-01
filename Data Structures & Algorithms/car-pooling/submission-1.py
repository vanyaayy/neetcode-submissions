class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        minHeap = []
        curPass = 0
        for t in trips:
            while minHeap and minHeap[0][0]<=t[1]:
                endT, pas = heapq.heappop(minHeap)
                curPass -=pas
            curPass+=t[0]
            if curPass>capacity:
                return False
            heapq.heappush(minHeap, (t[2], t[0]))
        return True
            
            