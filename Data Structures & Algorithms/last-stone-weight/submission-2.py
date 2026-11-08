class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>=2:
            if maxheap[0]==maxheap[1]:
                heapq.heappop(maxheap)
                heapq.heappop(maxheap)
            else:
                first = heapq.heappop(maxheap)
                sec = heapq.heappop(maxheap)
                heapq.heappush(maxheap, -(abs(first)-abs(sec)))
        return -maxheap[0] if maxheap else 0

        