class Solution:
    def climbStairs(self, n: int) -> int:
        hashMap = {}
        def dp(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 2
            else:
                if n in hashMap:
                    return hashMap[n]
                else:
                    hashMap[n] = dp(n-1)+dp(n-2)
                    return hashMap[n]
        return dp(n)

        