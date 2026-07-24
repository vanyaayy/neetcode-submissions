class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {} #value:index
        for i, n in enumerate(nums):
            if target-n in hashMap:
                return[hashMap[target-n], i]
            hashMap[n] = i
        
                    
        