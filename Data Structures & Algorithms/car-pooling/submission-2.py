class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        curPass = 0
        minHeap = []
        for t in trips:
            while minHeap and minHeap[0][0]<=t[1]:
                end, pas = heapq.heappop(minHeap)
                curPass-=pas
            heapq.heappush(minHeap, [t[2],t[0]]) 
            curPass+=t[0]
            if curPass>capacity:
                return False
        return True
        
        