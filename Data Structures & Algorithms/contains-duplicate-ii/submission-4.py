class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r = 0,0
        hashMap = defaultdict(int)
        while r<len(nums):
            if r-l>k:
                del hashMap[nums[l]]
                l+=1
            if nums[r] in hashMap:
            # if abs(hashMap[nums[r]]-r)<=k: no longer needed as
            # everything is within k
                return True

            hashMap[nums[r]]=r
            r+=1
        return False
       


        