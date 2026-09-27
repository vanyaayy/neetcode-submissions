class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r = 0
        hashMap = defaultdict(int)
        while r<len(nums):
            if nums[r] in hashMap:
                if abs(hashMap[nums[r]]-r)<=k:
                    return True

            hashMap[nums[r]]=r
            r+=1
        return False
       


        