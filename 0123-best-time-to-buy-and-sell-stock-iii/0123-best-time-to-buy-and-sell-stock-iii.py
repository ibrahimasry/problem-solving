class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1=buy2= inf
        sell1=sell2= -inf
        for p in prices:
            buy1 = min(buy1,p)
            sell1 = max(p-buy1,sell1)
            buy2 = min(p-sell1, buy2)
            sell2 = max(sell2, p - buy2)


        return sell2