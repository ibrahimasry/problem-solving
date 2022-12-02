class Solution:
    def numberOfWays(self, s: str) -> int:
        pattern1 = "101"
        pattern2 = "010"
        dp1 = [0] * 4
        dp2 = [0] * 4
        dp1[3] = 1
        dp2[3] = 1
        
        for c in s:
            for j in range(3):
                if c == pattern1[j]:
                    dp1[j] += dp1[j+1]
                if c == pattern2[j]:
                    dp2[j] += dp2[j+1]
        return dp1[0] + dp2[0]
        