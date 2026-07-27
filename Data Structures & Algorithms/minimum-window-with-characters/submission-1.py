class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":  #edge case
            return ""
        countT, window = defaultdict(int),defaultdict(int)
        for c in t:
            countT[c]+=1
        have, need = 0, len(countT) #countT gives unique chars in t
        res, resLen = [-1,-1], float("inf")
        l=0
        for i in range(len(s)):
            c=s[i]
            window[c]+=1
            if c in countT and window[c] == countT[c]:
                have+=1
            while have == need:
                #update result
                if i-l+1 < resLen:
                    res = [l,i]
                    resLen = i-l+1
                # pop from left
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,i = res
        return s[l:i+1] if resLen!=float("inf") else ""



            
        



        