class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = inf
        for price in prices:
            if price > prev:
                res += price - prev
                prev = price
            prev = min(price,prev)
        return res