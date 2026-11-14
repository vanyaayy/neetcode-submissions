class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for i in range(len(flowerbed)):
            left,right=-1,-1
            if i==0 or flowerbed[i-1]==0:
                left = 0
            if i==len(flowerbed)-1 or flowerbed[i+1]==0:
                right =0
            if flowerbed[i]==0 and left ==0 and right ==0:
                flowerbed[i]=1
                n-=1
            if n==0:
                return True
        return False
        