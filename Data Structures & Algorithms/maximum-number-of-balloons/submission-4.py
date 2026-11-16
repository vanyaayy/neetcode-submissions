class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)
        res=len(text)
        d = {"b":1,"a":1,"l":2,"o":2,"n":1}
        for i in text:
            hashmap[i]+=1
        
        for key, _ in d.items():
            if key not in hashmap:
                return 0 
            else:
                if d[key]==1:
                    res=min(res, hashmap[key])
                if d[key]==2:
                    res=min(res, hashmap[key]//2)
        return res

        
        