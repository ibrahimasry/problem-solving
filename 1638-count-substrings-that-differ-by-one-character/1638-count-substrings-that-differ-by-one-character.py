class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        hash = {}
        res = 0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                curr = s[i:j+1]
                m = 0
                l = len(curr)
                q = deque("-"+t[:len(curr)-1])
                while m < (len(t)-l) + 1:
                    found = 0
                    q.popleft()
                    q.append(t[(m+l) - 1])
                    for k in range(l):
                        if q[k] != curr[k] :
                            found += 1
                            if found > 1:
                                break
                    m += 1
                    if found != 1 :
                        continue
                    res += 1
        return res