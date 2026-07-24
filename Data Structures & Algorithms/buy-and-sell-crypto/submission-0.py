class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pricesCopy = prices[:]
        tmp =0
        for i in range(len(prices)-1):
            buy = pricesCopy.pop(0)
            sell = max(pricesCopy)
            profit = sell - buy
            if profit>tmp:
                tmp = profit


        return tmp

        