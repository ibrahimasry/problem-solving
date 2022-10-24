class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        
        @lru_cache(None)
        def dp(start, k):
            if start == n or n-start <= k :
                return 0
            
            count = defaultdict(int)
            ans = sys.maxsize
            maxChar = 0
            for j in range(start, n):
                c = s[j]
                count[c] += 1
                maxChar = max(count[c], maxChar)
                compressedLength = 1 + (len(str(maxChar)) if maxChar > 1 else 0)
                if k >= j - start + 1 - maxChar:
                    ans = min(ans, compressedLength + dp(j+1, k - (j - start + 1 - maxChar)))
            return ans
        n = len(s)
        return dp(0, k)
                    
        