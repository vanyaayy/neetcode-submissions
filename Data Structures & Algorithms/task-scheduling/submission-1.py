class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxheap = []
        time = 0
        q=deque()
        for k,v in freq.items():
            heapq.heappush(maxheap, -v)
        while maxheap or q:
            time+=1
            if maxheap:
                val = 1+heapq.heappop(maxheap)
                if val:
                    q.append((val,time+n))
            while q and time>=q[0][1]:
                f, t = q.popleft()
                heapq.heappush(maxheap, f)
        return time
            

        