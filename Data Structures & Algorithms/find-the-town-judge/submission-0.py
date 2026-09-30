class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = defaultdict(int)
        out = defaultdict(int)
        for src,dst in trust:
            inc[dst]+=1
            out[src]+=1

        for k,v in inc.items():
            if v==n-1:
                if out[k]==0:
                    return k
        return -1

        