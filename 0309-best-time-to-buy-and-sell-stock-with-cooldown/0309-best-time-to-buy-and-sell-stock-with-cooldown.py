class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cool = 0
        sell = 0
        buy = inf
        
        for p in prices:
            temp = sell
            buy = min(p - cool, buy)
            sell = max(p - buy,sell)
            cool = temp
        return sell