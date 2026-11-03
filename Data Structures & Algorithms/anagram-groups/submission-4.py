class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            arr = [0]*26
            for char in strs[i]:
                arr[ord(char)-ord('a')]+=1
            hashmap[tuple(arr)].append(strs[i]) #check
        return list(hashmap.values())

        