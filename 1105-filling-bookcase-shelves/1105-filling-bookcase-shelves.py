class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache(None)
        def dp(i, w, h):
            if i == n :
                return  h
            
            
            res =  h +  dp(i+1, shelfWidth - books[i][0] , books[i][1])
            
            if w - books[i][0] >= 0 :
                res = min(res, dp(i+1, w-books[i][0] , max(books[i][1], h)))
            return res
        n = len(books)
        return dp(0, 0, 0)