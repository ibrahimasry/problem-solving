class Solution:
    def countAnagrams(self, s: str) -> int:
        
        mod = 10 ** 9 + 7
        s = s.split()
        l = len(max(s,key=len))
        fact = [1] * (l+1)
        inv = [1] * (l+1)        
        for i in range(2,l+1):
            fact[i] = i * fact[i-1] % mod
            inv[i]  = pow(fact[i],-1,mod) % mod
        k = [Counter(c) for c in s]
        
        res = 1
        for i in range(len(s)):
            curr = fact[len(s[i])] 
            for c in k[i]:
                curr *= inv[k[i][c]] % mod
            curr %= mod
            res *= curr
            res %= mod
        return res
            
            
            