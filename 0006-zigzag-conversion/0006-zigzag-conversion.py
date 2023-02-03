class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res =  [""] * numRows
        
        down = True
        i = 0
        r = 0
        while i < len(s):
            res[r] += s[i]
            if  down :
                r += 1
                if r == numRows-1:
                    down = False

            else:
                r -= 1
                if r <= 0:
                    down = True

            i+= 1
        return "".join(res)
                