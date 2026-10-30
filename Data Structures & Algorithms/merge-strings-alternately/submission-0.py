class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        merged = ""
        minWord = min(len(word1), len(word2))
        while l<minWord:
            merged+=word1[l]+word2[l]
            l+=1
        if l==len(word1):
            merged+=word2[l:]
        else:
            merged+=word1[l:]
        
        return merged



        