class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        res = 1
        for i in range(n-1):
            res = one+two
            two = one
            one = res
        return res

        