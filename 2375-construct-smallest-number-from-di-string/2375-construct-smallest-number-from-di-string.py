class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        res = []
        
        for i, c in enumerate(pattern+"I",1):
            
            if c == "I":
                res += range(i, len(res), -1)
        return "".join(map(str, res))
        