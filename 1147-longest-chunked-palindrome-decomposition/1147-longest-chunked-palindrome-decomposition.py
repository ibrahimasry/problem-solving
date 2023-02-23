class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        r = ''
        l = ''
        for a1,a2 in zip(text,text[::-1]):
            l = l + a1
            r = a2 + r
            if l == r:
                res += 1
                l = r = ''
        return res