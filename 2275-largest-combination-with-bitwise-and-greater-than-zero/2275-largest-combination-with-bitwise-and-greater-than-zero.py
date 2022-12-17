class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        dp = [0] * 32
        
        for n in candidates:
            for i in range(32):
                if n >> i & 1:
                    dp[i] += 1
        return max(dp)