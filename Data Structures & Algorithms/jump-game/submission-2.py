class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l= len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=(l-i):
                l =i
        if l==0:
            return True
        else:
            return False

        