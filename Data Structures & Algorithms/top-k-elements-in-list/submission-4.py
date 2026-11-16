class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap =defaultdict(int)
        res=[]
        arr = [[] for i in range(len(nums)+1)]
        for i in nums:
            hashmap[i]+=1 #ele->freq
        for key, val in hashmap.items():
            arr[val].append(key) #freq->[ele]
        for i in range(len(nums),0,-1):
            for ele in arr[i]:
                res.append(ele)
                if len(res)==k:
                    return res




        
        