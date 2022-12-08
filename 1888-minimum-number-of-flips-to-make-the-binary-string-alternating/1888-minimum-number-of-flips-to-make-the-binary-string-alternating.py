class Solution:
    def minFlips(self, s: str) -> int:
        s = s + s
        s = [int(c) for c in s]
        def good(s):
            
            prefix = [0]
            res = len(s)
            for i, c in enumerate(s):
                if i % 2 == c:
                    prefix.append(prefix[-1])
                else :
                    prefix.append(prefix[-1] + 1)
                
                if i >= (len(s) // 2):
                            
                    res = min(res, prefix[-1] - prefix[-1-(len(s)//2)])
            
            return res
        r = [1-c for c in s]
        return min(good(s), good(r))