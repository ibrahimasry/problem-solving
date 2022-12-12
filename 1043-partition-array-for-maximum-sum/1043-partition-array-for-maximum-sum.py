class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        
        n = len(arr)
        dp = [0] * n
        
        
        for i in range(n):
            curr = -sys.maxsize
            for j in range(k):
                if i - j < 0 :
                    continue
                prev = arr[i-j] if i - j >= 0 else 0
                curr = max(curr, prev)
                prevArr = dp[i-j-1] if i-j-1 >= 0 else 0
                dp[i] = max(curr * (j+1) + prevArr, dp[i])
                
        return dp[-1]