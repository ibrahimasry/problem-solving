class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        
        ans = 0
        s = str(n)
        strLen = len(str(n))
        digitsLen = len(digits)
        
        for i in range(1,strLen):
            ans += digitsLen ** i
        dp = [0] * strLen
        
        for i in range(strLen -1, -1, -1):
            for d in digits:
                if d < s[i]:
                    dp[i] += digitsLen ** (strLen-i-1)
                elif d == s[i]:
                    dp[i] += dp[i+1] if i + 1 < strLen else 1
        return dp[0] + ans