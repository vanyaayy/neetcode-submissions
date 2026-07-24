from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0]*26 #a..z
            for chars in word:
                count[ord(chars)-ord("a")]+=1
            res[tuple(count)].append(word)
        return list(res.values())

         
            
        