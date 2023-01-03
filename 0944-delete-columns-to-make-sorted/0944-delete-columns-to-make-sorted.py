class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        m = len(s)
        n = len(s[0])
        res = 0
        seen = set()
        for i in range(1,m):
            for j in range(n):
                if s[i][j] < s[i-1][j]:
                    seen.add(j)
        return len(seen)