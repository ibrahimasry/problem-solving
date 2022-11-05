class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        
        
        @lru_cache(None)
        def dp(index, isPrefix1, isPrefix2, currEvilLength):
            if currEvilLength == len(evil):
                return 0
            if index == n:
                return 1
            start = ord(s1[index]) if isPrefix1 else ord('a')
            end = ord(s2[index]) if isPrefix2 else ord('z')
            ans = 0
            for i in range(start, end+1):
                tempLength = currEvilLength
                c = chr(i)
                while tempLength > 0 and evil[tempLength]  != c:
                    tempLength = lsp[tempLength - 1]
                if evil[tempLength] == c:
                    tempLength += 1
                ans += dp(index + 1 , isPrefix1 and c == s1[index], isPrefix2 and c == s2[index], tempLength)
            return ans
        lsp = [0] * len(evil)
        
        i = 1
        j = 0
        
        while i < len(evil):
            while j > 0 and evil[i] != evil[j]:
                j = lsp[j-1]
            if evil[i] == evil[j]:
                j += 1
                lsp[i]=j
            i += 1
        return dp(0, True, True, 0) % (10 ** 9 + 7)

        