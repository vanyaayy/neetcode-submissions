class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = defaultdict(int)
        s1 = {"b":1,"a":1,"l":2,"o":2,"n":1}
        count =0
        for i in text:
            if i in s1:
                hashmap[i]+=1
            if hashmap["b"]>=1 and hashmap["a"]>=1 and hashmap["l"]>=2 and hashmap["o"]>=2 and hashmap["n"]>=1:
            
                count+=1
                for key,val in s1.items():
                    hashmap[key]-=val
        return count

      