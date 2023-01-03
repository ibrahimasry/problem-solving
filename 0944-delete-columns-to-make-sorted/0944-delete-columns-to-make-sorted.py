class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        m = len(s)
        n = len(s[0])
        res = 0
        for j in range(n):
            for i in range(1,m):
                if s[i][j] < s[i-1][j]:
                    res += 1
                    break
        return res