class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for i in strs:
            charArr = [0]*26
            for char in i:
                charArr[ord(char)-ord('a')]+=1
            hashMap[tuple(charArr)].append(i)
        
        return (list(hashMap.values()))

        