class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @cache
        def dp(i,j,diff):
            if i == len(s1) and j == len(s2):
                return diff == 0
            if i < len(s1) and s1[i].isdigit():
                start = i
                while i < len(s1) and s1[i].isdigit():
                    if dp(i+1,j,diff + int(s1[start:i+1])):
                        return True
                    i += 1
            elif  j < len(s2) and s2[j].isdigit():
                start = j
                while j < len(s2) and s2[j].isdigit():
                    if dp(i,j+1,diff-int(s2[start:j+1])):
                        return True
                    j += 1
            elif i < len(s1) and diff < 0 :
                if dp(i+1, j ,diff + 1):
                    return True
            elif j < len(s2) and diff > 0 :
                if dp(i,j+1,diff-1):
                    return True
            elif i < len(s1) and j < len(s2) and s1[i] == s2[j] and diff == 0:
                if dp(i+1,j+1,diff):
                    return True
            return False
        return dp(0,0,0)
            