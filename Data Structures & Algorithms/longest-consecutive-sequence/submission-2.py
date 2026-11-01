class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        longest = 0
        for i in arr:
            if i-1 in arr:
                continue
            else:
                j=i
                while j in arr:
                    j+=1
                    longest = max(longest, j-i)
        return longest
            


        