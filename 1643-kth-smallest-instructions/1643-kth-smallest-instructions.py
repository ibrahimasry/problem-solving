class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        
        v, h = destination
        res = ""
        length = h + v
        for i in range(length):
            startWithK = comb(length-i-1, v)
            if k <= startWithK:
               res += "H"
            else :
                k -= startWithK
                res += "V"
                v -= 1
        return res
        