class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        mapped = defaultdict(set)
        for k , v in mappings:
            mapped[k].add(v)
        
        for i in range(len(s) - len(sub) + 1):
            for k in range(len(sub)):
                c = s[i+k]
                c1 = sub[k] 
                
                if c1 != c and not (c1 in mapped and c in mapped[c1]):
                    break
                
                if k == len(sub)-1:
                    return True

        return False
            
                