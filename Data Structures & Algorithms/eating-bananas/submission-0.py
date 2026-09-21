class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)-1
        optimal = max(piles)-1
        while l<=r:
            mid =(l+r)//2
            hours = 0
            for i in piles:
                hours+= math.ceil(i/(mid+1))
            if hours <= h:
                optimal = min(optimal, mid)
                r = mid - 1
            elif hours > h:
                l = mid+1
        return optimal+1

        