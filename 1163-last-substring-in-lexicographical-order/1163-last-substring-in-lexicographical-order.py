class Solution:
    def lastSubstring(self, s: str) -> str:
        
        
        maxc = max(s)
        cand = [i for i, c in enumerate(s) if c == maxc]
        n = len(s)
        offset = 1
        while len(cand) > 1 :
            nextcand = []
            nextc = max(s[st+offset] for i, st in enumerate(cand) if st + offset < n)
            for i, st in enumerate(cand):
                if i > 0 and cand[i-1] + offset == st:
                    continue
                if st + offset < n and s[st+offset] == nextc:
                    nextcand.append(st)
            offset += 1
            cand = nextcand
        return s[cand[0]:]