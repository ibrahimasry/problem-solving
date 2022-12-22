class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def valid(s1,s2):
            for x, y in zip(sorted(s1),sorted(s2)):
                if x < y:
                    return False
            return True
        return valid(s1,s2) or valid(s2,s1)