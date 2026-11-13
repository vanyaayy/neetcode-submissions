class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        final = 0
        while l<=r:
            mid = (l+r)//2
            ships = 1
            s= mid
            for w in weights:
                if (s-w)<0:
                    ships+=1
                    s=mid
                s=s-w
            if ships<=days:
                r=mid-1
                final = mid
            else:
                l =mid+1
        return final

        