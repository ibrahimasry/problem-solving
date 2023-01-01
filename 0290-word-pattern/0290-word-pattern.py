class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapped = dict()
        mapped2 = dict()
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i,c in enumerate(pattern):
            match = s[i]
            if c in mapped and mapped[c] != match:
                return False
            if match in mapped2 and mapped2[match] != c:
                return False
            if c not in mapped:
                mapped[c] = match
                mapped2[match] = c
        return True