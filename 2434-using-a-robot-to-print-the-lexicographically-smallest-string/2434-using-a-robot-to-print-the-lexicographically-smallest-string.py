class Solution:
    def robotWithString(self, s: str) -> str:
        
        def low(feq):
            values = [c for c in feq.keys() if freq[c] > 0]
            
            return "z" if len(values) == 0 else sorted(values)[0]
            
        freq = Counter(s)
        stack = []
        ans = []
        
        for c in s:
            
            stack.append(c)
            freq[c] -= 1
            
            while stack and stack[-1] <= low(freq):
               ans += stack.pop()
        return "".join(ans)