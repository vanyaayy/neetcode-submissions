class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        res =[] 
        hashmap = defaultdict(int) #ele -> freq
        for i in nums:
            hashmap[i]+=1
        for key, val in hashmap.items():
            arr[val].append(key)
        for i in range(len(arr)-1,0,-1):
            for el in arr[i]:
                res.append(el)
                if len(res)==k:
                    return res

        