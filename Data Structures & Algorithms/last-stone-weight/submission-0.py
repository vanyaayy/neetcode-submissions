class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second>first: #since vals r neg in heap
                heapq.heappush(stones, -(abs(first)-abs(second)))
        
        return -stones[0] if stones else 0
                