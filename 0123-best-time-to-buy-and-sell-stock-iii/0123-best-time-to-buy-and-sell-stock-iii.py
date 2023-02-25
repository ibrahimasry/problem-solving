class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = [-inf] * 4
        for p in prices:
            prev[0] = max(-p,prev[0])
            prev[1] = max(prev[1] , p + prev[0])
            prev[2] = max(-p + prev[1], prev[2] )
            prev[3] = max(prev[3] , p + prev[2])
        return prev[-1]