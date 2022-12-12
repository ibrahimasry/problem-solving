class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        
        n = len(arr)
        dp = [0] * (n+1)
        
        
        for i in range(1, n + 1):
            curr = -sys.maxsize
            for j in range(k):
                if i - j - 1 >= 0 :
                    curr = max(curr, arr[i-j-1])
                    dp[i] = max(curr * (j+1) +  dp[i-j-1] , dp[i])
                
        return dp[-1]