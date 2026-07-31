class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxP