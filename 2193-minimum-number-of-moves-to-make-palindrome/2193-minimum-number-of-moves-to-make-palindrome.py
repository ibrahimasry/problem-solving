class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            l = s.index(s[-1])
            if l != len(s) - 1:
                res += l
                s.pop(l)
            else :
                res += len(s) // 2
            s.pop()

        return res