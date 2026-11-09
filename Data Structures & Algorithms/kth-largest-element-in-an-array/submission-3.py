class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for ele in nums:
            if len(minheap)==k:
                if ele>minheap[0]:
                    heapq.heappop(minheap)
                else:
                    continue
            heapq.heappush(minheap, ele)
        return minheap[0]

        