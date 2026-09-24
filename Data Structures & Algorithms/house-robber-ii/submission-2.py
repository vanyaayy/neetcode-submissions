class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        value = max(nums[0], self.helper(nums[0:length-1]), self.helper(nums[1:length]))
        return value
        
    def helper(self, nums):
        rob1,rob2=0,0
        for n in nums:
            temp = max(rob1+n, rob2)                
            rob1= rob2
            rob2= temp
        return rob2
        
