class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = defaultdict(int)
        q = deque()
        time=0
        for i in tasks:
            hashmap[i]+=1
        maxheap = [-val for _, val in hashmap.items()]
        heapq.heapify(maxheap)
        while maxheap or q:
            if maxheap:
                freq = heapq.heappop(maxheap)
                freq+=1
                time+=1
                if freq!=0:
                    q.append((freq, time+n))
            else:
                time=q[0][1]
            if q:
                if time==q[0][1]:
                    f, t=q.popleft()
                    heapq.heappush(maxheap, f)
        return time

            

        
        