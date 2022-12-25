class Solution:
    def maximumTastiness(self, prices: List[int], k: int) -> int:
        prices.sort()
        def good(diff):
            prev = prices[0]
            count = 1
            for i in range(1, len(prices)):
                if prices[i] - prev >= diff:
                    count += 1
                    prev = prices[i]
            return count >=k
        l = 0
        r = prices[-1]
        
        while l < r:
            m= (l+r+1) >> 1
            if good(m):
                l = m
            else :
                r = m - 1
        
        
        return l