class Solution:
    def minDeletions(self, s: str) -> int:
        count = (Counter(s).values())
        res = 0
        seen = set()
        for  n in count:
            if n not in seen:
                seen.add(n)
            else :
                i = n-1
                while i and i in seen:
                    i -= 1
                if i != 0:
                    seen.add(i)
                res += n - i
        return res