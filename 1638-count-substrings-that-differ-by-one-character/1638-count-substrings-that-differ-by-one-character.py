class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        hash = {}
        res = 0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                m = 0
                l = j - i + 1
                while m < (len(t)-l) + 1:
                    found = 0
                    for k in range(l):
                        if t[m+k] != s[i + k] :
                            found += 1
                            if found > 1:
                                break
                    m += 1
                    if found != 1 :
                        continue
                    res += 1
        return res