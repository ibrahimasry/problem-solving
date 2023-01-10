class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        count = Counter()
        res = 0
        start = 0
        frog = 'croak'
        for i in range(len(s)):
            c = s[i]
            count[c] += 1
            j = frog.index(c)
            if c == "c":
                start += 1
                res = max(start,res)
            elif count[frog[j-1]] - 1 < 0:
                return -1
            else:
                count[frog[j-1]] -= 1
            if j == 4:
                start -= 1
        if start > 0:
            return -1
        return  res