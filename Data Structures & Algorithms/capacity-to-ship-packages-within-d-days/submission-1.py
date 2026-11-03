class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r
        while l<=r:
            d=1
            mid = (l+r)//2
            m = mid
            for i in weights:
                if mid-i <0:
                    d+=1
                    mid = (l+r)//2
                mid=mid-i
            if d>days:
                l = m+1
            else:
                res = min(res, m)
                r=m-1
        return res
        
        