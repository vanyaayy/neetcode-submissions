class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        hashmap = defaultdict(int)
        have = defaultdict(int)
        l,r =0, len(s1)-1
        for i in range(len(s1)):
            hashmap[s1[i]]+=1
            have[s2[i]]+=1
        while r<len(s2):
            if have==hashmap:
                return True
            have[s2[l]]-=1
            if have[s2[l]]==0:
                del have[s2[l]]
            l+=1
            r+=1
            if r<len(s2):
                have[s2[r]]+=1
        
        return False

        



        
        