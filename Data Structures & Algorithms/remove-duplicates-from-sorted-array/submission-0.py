class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r =0,1
        while r<len(nums):
            if nums[l]!=nums[r]:
                l=r
                r+=1
            else:
                while r<len(nums) and nums[l]==nums[r]:
                    nums.pop(r)
                   
        return len(nums)


        