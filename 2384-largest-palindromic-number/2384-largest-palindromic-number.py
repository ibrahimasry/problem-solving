class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        
        pal = ""
        
        for i in range(9,-1,-1):
            if count[str(i)] > 1:
                if i == 0 and not pal:
                    break
                pal += str(i) *  int(count[str(i)] //2)
        for i in range(9,-1,-1):
            if count[str(i)] % 2:
                return str(int(pal + str(i) + pal[::-1]))
        if not pal:
            return '0'
        return str(int(pal + pal[::-1]))