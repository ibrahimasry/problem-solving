class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dp(s1,s2):
            if not s1:
                return True
            if len(s1) == 1:
                return s1 == s2
            if s1 == s2:
                return True
            if Counter(s1) != Counter(s2):
                return False
            for i in range(1,len(s1)):
                if dp(s1[:i],s2[:i]) and dp(s1[i:],s2[i:]):
                    return True
                if dp(s1[:i],s2[-i:]) and dp(s1[i:],s2[:-i]):
                    return True
            return False
        return dp(s1,s2)