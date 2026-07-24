class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final =[]
        for counter, num in enumerate(nums):
            l = counter +1
            r = len(nums)-1
            if counter>0 and num ==nums[counter-1]:
                continue
            while l<r:
                if num+nums[l]+nums[r]<0:
                    l+=1
                elif num+nums[l]+nums[r]>0:
                    r-=1
                else:
                    final.append([num, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return final

                    




        