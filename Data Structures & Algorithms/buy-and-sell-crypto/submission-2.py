class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = 0
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[minVal]:
                minVal = r                
            res = max(res, (prices[r]-prices[minVal]))
        return res