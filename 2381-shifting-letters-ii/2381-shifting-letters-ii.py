class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        dp = [0] * (n+1)
        
        curr = 0
        shifts.sort()
        
        for start, end, to in shifts:
            dp[end + 1] += (-1 if to == 1 else 1)
            dp[start] += (1 if to == 1 else -1)
        ans = ""
        curr = 0
        for i, c in enumerate(s):
            curr += dp[i]
            rev = (ord(c) - ord("a") + curr + 26) % 26
            ans += chr(rev + ord("a"))
        return ans 