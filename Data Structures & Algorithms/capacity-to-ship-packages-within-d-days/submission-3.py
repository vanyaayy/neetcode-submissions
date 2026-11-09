class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        ships = 0
        res = 0
        while l<=r:
            mid = (l+r)//2
            total = 0
            ships=1
            for i in weights:
                if total+i>mid:
                    ships+=1
                    total=0
                total+=i
                
            if ships<=days:
                res = mid
                r=mid-1
            else:
                l=mid+1
        return res
        