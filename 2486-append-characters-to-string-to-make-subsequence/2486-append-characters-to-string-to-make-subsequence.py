class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        n = len(s)
        m = len(t)
        
        for i in range(n):
            if s[i] == t[j]:
                j += 1
                if j == m :
                    return 0
        return m - j
        