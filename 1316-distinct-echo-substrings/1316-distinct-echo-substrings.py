class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        
        
        def getHash(start, end):
            if start == 0:
                return hash[end]
            return hash[end] - hash[start-1] * powers[end-start + 1]
        mod = (10**9) + 7
        n = len(text)
        hash = [0] * (n)
        powers = [0] * (n)
        prevHash = 0
        prevPower = 1
        for i, c in enumerate(text):
            code = ord(c) 
            hash[i] = prevHash = (prevHash * 256 + code) % mod
            powers[i] = prevPower = 1 if i == 0 else  prevPower * 256 % mod
        seen = set()
        for i , c in enumerate(text):
            for l in range(2, n+1, 2):
                if i + l > n:
                    break
                mid = i + l//2 -1
                s1= getHash(i, mid) % mod
                s2 = getHash(mid+1, i+l-1) % mod
                if s1 == s2:
                    seen.add(s1)
        return len(seen)