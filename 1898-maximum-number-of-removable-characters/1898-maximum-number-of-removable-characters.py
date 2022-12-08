class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l = 0
        r = len(removable) 
        def good(k):
            seen = set(removable[:k])
            n2 = len(s)
            n1 = len(p)
            j = 0
            for i in range(n2):
                if not (i in seen) and s[i] == p[j]:
                    j += 1
                    if j == n1:
                        return True
            return False
        while l < r:
            
            m = l + (r - l + 1) // 2
            
            if good(m):
                l = m 
            else :
                r = m - 1
        return l  if good(l) else 0