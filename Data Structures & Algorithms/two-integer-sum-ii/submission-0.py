class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap= {} #value:index
        for i, n in enumerate(numbers):
            if target-n in hashMap:
                return[hashMap[target-n]+1, i+1]
            hashMap[n] = i
        