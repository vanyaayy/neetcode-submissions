class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l =0
        sum = 0
        window = len(nums)+1
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                window = min(window, r-l+1)
                sum-=nums[l]
                l+=1
        return window if window <len(nums)+1 else 0

        


        