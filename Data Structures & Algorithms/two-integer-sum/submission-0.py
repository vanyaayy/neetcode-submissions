class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a =[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]+nums[j]==target and i!=j):
                    a.append(i)
                    a.append(j)
                    return a
                    
        