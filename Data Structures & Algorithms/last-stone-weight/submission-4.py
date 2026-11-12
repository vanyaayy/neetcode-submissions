import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st = [-stone for stone in stones]
        heapq.heapify(st)
        while len(st)>=2:
            first = heapq.heappop(st) #neg
            second = heapq.heappop(st)
            if first!=second:
                heapq.heappush(st, (first-second))
        
        return -st[0] if len(st)>0 else 0



        