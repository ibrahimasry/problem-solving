class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        
        dp = [0,0,1,1]
        r = 1
        for i in range(1, len(pressedKeys)):
            if pressedKeys[i] == pressedKeys[i-1]:
                r += 1
            else :
                r = 1
            l = min(r, 4 if pressedKeys[i] in "97" else 3)
            dp = dp[1:] + [sum(dp[-l:])]
        return dp[-1] % (10**9 +7)