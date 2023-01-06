class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        res = 0
        ls = len(s)
        lt = len(t)
        
        for i in range(ls):
            for j in range(i,ls):
                m = 0
                l = j - i + 1
                for m in range(lt - l + 1):
                    found = 0
                    for k in range(l):
                        if t[m+k] != s[i + k] :
                            found += 1
                            if found > 1:
                                break
                    if found == 1 :
                        res += 1

        return res