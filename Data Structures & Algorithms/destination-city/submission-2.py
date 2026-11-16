from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap=defaultdict(int)
        for src, _ in paths:
            hashmap[src]+=1
        for _, dest in paths:
            if dest not in hashmap:
                return dest
        

