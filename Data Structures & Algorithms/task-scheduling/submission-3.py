class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)
        time =0
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        while maxheap or q:
            time+=1
            if maxheap:
                cnt = heapq.heappop(maxheap)
                if cnt+1!=0:
                    q.append((cnt+1, time+n))
            if q:
                if time == q[0][1]:
                    c, t = q.popleft()
                    heapq.heappush(maxheap, c)
        return time



        