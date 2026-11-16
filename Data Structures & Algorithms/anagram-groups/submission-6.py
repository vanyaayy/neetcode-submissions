class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            arr = [0]*26
            for char in i:
                arr[ord(char)-ord('a')]+=1
            hashmap[tuple(arr)].append(i)
        return list(hashmap.values())


        