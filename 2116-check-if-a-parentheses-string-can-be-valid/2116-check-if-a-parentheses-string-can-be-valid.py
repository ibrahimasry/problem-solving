class Solution:
    def canBeValid(self, s: str, lockes: str) -> bool:
        open = 0
        if len(s) % 2 :
            return False

        for i, c in enumerate(s):
            if lockes[i] == "0" or c == '(':
                open += 1
            else :
                open -= 1
            if open < 0:
                return False
        open = 0

        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if lockes[i] == "0" or c == ')':
                open += 1
            else :
                open -= 1
            if open < 0:
                return False

        return open >= 0

