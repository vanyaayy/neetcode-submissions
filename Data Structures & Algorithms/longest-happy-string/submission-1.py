class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res =""
        maxheap = []
        for count,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count!=0:
                heapq.heappush(maxheap, (count,char))
        while maxheap:
            freq, char= heapq.heappop(maxheap)
            if res!="" and len(res)>=2:
                if res[-1]==char and res[-2]==char:
                    if maxheap:
                        freq2, char2 = heapq.heappop(maxheap)
                        res+=char2
                        freq2+=1
                        if freq2!=0:
                            heapq.heappush(maxheap, (freq2,char2))
                    else:
                        return res
            res+=char
            freq+=1
            if freq!=0:
                heapq.heappush(maxheap, (freq,char))
        return res

        