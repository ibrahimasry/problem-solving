class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        
        v, h = destination
        res = ""
        length = h + v
        for i in range(length):
            startWithH = comb(length-i-1, v)
            if k <= startWithH:
               res += "H"
            else :
                k -= startWithH
                res += "V"
                v -= 1
        return res
        