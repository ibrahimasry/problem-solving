class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            currWidth = shelfWidth
            currHeight = 0
            for j in range(i,0,-1):
                w, h = books[j-1]
                if currWidth - w < 0:
                    break
                currWidth  -= w
                currHeight = max(currHeight, h)
                dp[i] = min(dp[i], dp[j-1] + currHeight)
        return dp[-1]