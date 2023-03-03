class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        base = 97
        power = 0
        
        window = 0
        window2 = 0
        
        for i, c in enumerate(needle):
            c2 = haystack[i]
            window = window * base + (ord(c) - ord('a'))
            window2 = window2 * base + (ord(c2) - ord('a'))
            if power == 0:
                power = 1
            else:
                power *= base

        if window == window2:
            return 0
        m = len(needle)
        for i in range(len(needle) , len(haystack)):
            window2 -= (ord(haystack[i-m])- ord('a')) * power
            window2 = window2 * base + (ord(haystack[i]) - ord('a'))
            if window2 == window:
                return i - m + 1
        return -1