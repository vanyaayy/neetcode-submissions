class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = defaultdict(int)
        hm = defaultdict(int)
        l, r =0,0
        for char in s1:
            hashmap[char]+=1
        while r<len(s2):
            hm[s2[r]]+=1
            if (r-l+1)==len(s1):
                if hashmap==hm:
                    return True
                else:
                    hm = defaultdict(int)
                    l+=1
                    r=l
                    if r<len(s2):
                        hm[s2[r]]+=1
                    else:
                        return False
            r+=1
        return False
                




        