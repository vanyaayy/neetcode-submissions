class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r =0,0
        res = 0
        hashmap = defaultdict(int)
        while r<len(s):
            hashmap[s[r]]+=1
            while hashmap[s[r]]>1:
                hashmap[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
           


        