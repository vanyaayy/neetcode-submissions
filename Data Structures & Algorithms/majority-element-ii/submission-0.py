class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        res=[]
        freq = len(nums)//3
        for i in nums:
            hashMap[i]+=1
        for k,v in hashMap.items():
            if v>freq:
                res.append(k)
        return res
        