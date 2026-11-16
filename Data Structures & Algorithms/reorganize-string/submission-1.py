class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = defaultdict(int)
        prev =None
        res=""
        for i in s:
            hashmap[i]+=1
        maxheap = [(-cnt, char) for char, cnt in hashmap.items()]
        heapq.heapify(maxheap)
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt, char = heapq.heappop(maxheap)
            res+=char
            cnt+=1
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt!=0:
                prev = (cnt, char)
        return res



        