class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)
        word = word1 + word2
        dp = [[0] * len(word) for _ in word]
        res = 0
        for i in range(len(word) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(word)):
                if word[i] == word[j]:
                    if   j - i < 2 :
                        dp[i][j] =  2
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                    if i < n1 and j >= n1:
                        res = max(res, dp[i][j])
                else :
                    dp[i][j] = max(dp[i+1][j] , dp[i][j-1])
        return res