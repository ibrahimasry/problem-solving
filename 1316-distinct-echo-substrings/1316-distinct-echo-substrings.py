class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        mod = (10**9) + 7
        n = len(text)
        hash = [0] * (n+1)
        powers = [0] * (n+1)
        
        powers[0] = 1
        
        for i, c in enumerate(text):
            code = ord(c) 
            hash[i+1] = (hash[i] * 256 + code) % mod
            powers[i+1] = (powers[i] * 256) % mod
        seen = set()
        for i , c in enumerate(text):
            for l in range(2, n+1, 2):
                if i + l > n:
                    break
                f = i + l // 2
                s1 = ((hash[f] - hash[i] * powers[(f-i)] % mod) + mod) % mod
                s2 = ((hash[i+l] - hash[f] * powers[((i+l)-f)] % mod) + mod) % mod
                if s1 == s2:
                    seen.add(s1)
        return len(seen)