class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        res = 0
        for p in prices:
            mn = min(p, mn)
            res = max(res,p - mn)
        return res