class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        negative = True if n[0] == "-" else False
        
        
        n = [int(c) for c in n if c != "-"]
        
        
        for i in range(len(n)):
            
            if negative:
                if n[i] > x:
                    return "-" + "".join([str(c) for c in n[:i] + [x] + n[i:]])
            elif n[i] < x:
                return "".join([str(c) for c in n[:i] + [x] + n[i:]])
        if negative:
            return "-" + "".join([str(c) for c in n + [x]])
        return  "".join([str(c) for c in n + [x]])
            