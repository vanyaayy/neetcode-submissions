class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj1=defaultdict(list) # x trusts -> y
        adj2=defaultdict(list) # x is trusted by ->
        for inc, out in trust:
            adj1[inc].append(out)
            adj2[out].append(inc)
        
        for k,v in adj2.items():
            if k not in adj1 and len(v)==n-1:
                return k
        return -1

            

        