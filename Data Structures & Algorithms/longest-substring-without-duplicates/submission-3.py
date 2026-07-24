class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        longest = ""
        max_len = 0
        while(r<len(s)):
            if(s[r] not in longest):
                longest = longest + s[r]
                max_len = max(max_len,len(longest))
                r=r+1
            else:
                longest=""
                l=l+1
                r=l
        return max_len



                

        