class Solution:
    def reformatNumber(self, number: str) -> str:
        
        arr = [n for n in number if n.isdigit()]
        res = ''
        
        i = 0
        count = len(arr)
        while i < len(arr):
            k = 2
            if (count - 3) >= 2 or count - 3 == 0:
                k = 3
                count -= 3
            else :
                k = 2
                count -= 2
            while k:
                res += arr[i]
                i += 1
                k -= 1
            if count == 0:
                return res
            res += '-'
        return res