class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set(nums)
        if len(dupe)<len(nums):
            return True
        else:
            return False
        