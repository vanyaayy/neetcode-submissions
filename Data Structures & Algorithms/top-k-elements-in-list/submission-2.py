class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res=[]
        arr = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        for key,v in hashmap.items():
            arr[v].append(key)
        for i in range(len(arr)-1,0,-1):
            for ele in arr[i]:
                res.append(ele)
                if len(res)==k:
                    return res
                    
                  
