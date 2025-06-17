class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        res = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
                continue
            res = max(res, price - minPrice)
        return res
