class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
        
        @lru_cache(2000)
        def dp(i,j):
            
            if i >= j :
                return 0
            curr = 0
            if i == 0:
                curr = prefix[j]
            else :
                curr= prefix[j] - prefix[i-1]
            return max(curr - stones[i] - dp(i+1,j), curr - stones[j] - dp(i,j-1))
        
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1,n):
            prefix[i] += prefix[i-1] + stones[i]

        return dp(0, n-1)