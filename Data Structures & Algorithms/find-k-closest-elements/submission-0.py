class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while r-l+1>k:
            dist1 = abs(x-arr[l])
            dist2 = abs(x-arr[r])
            if dist1>dist2:
                l+=1
            else:
                r-=1
        return arr[l:r+1]

        