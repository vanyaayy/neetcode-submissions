class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #l =buy, r = sell
        profit = 0
        while r<len(prices):
            if (prices[l]>prices[r]):
                l+=1
                r = l+1
            else:
                if (prices[r]-prices[l]>profit):
                    profit = prices[r]-prices[l]
                r+=1
        return profit
            


     

        