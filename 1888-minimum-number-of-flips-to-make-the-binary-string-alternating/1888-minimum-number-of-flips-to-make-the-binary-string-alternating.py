class Solution:
    def minFlips(self, s: str) -> int:
        s = s + s
        s = [int(c) for c in s]
        def good(flip):
            
            prefix = [0]
            res = len(s)
            for i, c in enumerate(s):
                if flip == c:
                    prefix.append(prefix[-1])
                else :
                    prefix.append(prefix[-1] + 1)
                
                if i >= (len(s) // 2) - 1:
                            
                    res = min(res, prefix[-1] - prefix[-1-(len(s)//2)])
                flip ^= 1
            return res
        return min(good(0), good(1))