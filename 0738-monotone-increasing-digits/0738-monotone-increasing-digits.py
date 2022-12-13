class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        
        s = str(n)
        res = ""
        n = len(s)
        i = 1
        while i < n:
            j = i
            
            while j < n and s[j] == s[j-1]:
                j += 1
            if j == n:
                return int(s)
            if s[j] < s[j-1] :
                return int(s[:i-1] + str((int(s[i-1]) - 1)) + "".join(['9'] * (len(s) - i)))
            i = j+1
        return int(s)