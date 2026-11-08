class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out = defaultdict(int)
        inc = defaultdict(int)
        for src, dest in trust:
            out[src]+=1
            inc[dest]+=1
        for i in range(1, n+1):
            if inc[i]==n-1 and out[i]==0:
                return i

        return -1


        