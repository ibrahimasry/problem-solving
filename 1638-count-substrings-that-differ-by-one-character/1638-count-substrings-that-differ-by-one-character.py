class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        hash = {}
        res = 0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                curr = s[i:j+1]
                m = 0
                l = len(curr)
                while m < (len(t)-len(curr)) + 1:
                    found = 0
                    org = t[m:m+len(curr)]
                    for c1,c2 in zip(curr, org):
                        if c1 != c2 :
                            found += 1
                            if found > 1:
                                break
                    m += 1
                    if found != 1 :
                        continue
                    res += 1
        return res