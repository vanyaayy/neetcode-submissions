class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>=2:
            first = heapq.heappop(maxheap)
            sec = heapq.heappop(maxheap)
            if first!=sec:
                heapq.heappush(maxheap, -(abs(first)-abs(sec)))
        return -maxheap[0] if maxheap else 0

        