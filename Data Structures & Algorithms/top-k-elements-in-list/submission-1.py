from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res= defaultdict(int)
        freq =[[] for n in range(len(nums)+1)]
        final =[]
        for number in nums:
            res[number]+=1
        for key,v in res.items():
            freq[v].append(key)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                final.append(n)
                if len(final)==k:
                    return final

