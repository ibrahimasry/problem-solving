class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        s = [''] * len(lcp[0])
        
        ascii = 0
        
        r = len(lcp)
        c = len(lcp[0])
        
        for i in range(r):
            if  s[i] != "":
                continue
            if ascii > 25:
                return ''

            for j in range(i,c):
                if lcp[i][j] :
                    s[j] = chr(ord('a') + (ascii))
            ascii += 1

        for i in range(r):
            for j in range(c):
                ahead = lcp[i+1][j+1] if i + 1 < r and j + 1 < c  else 0
                aheadVal = 0 if s[j] != s[i] else ahead + 1
                if  lcp[i][j]  != aheadVal:
                    return ''
        return ''.join(s)