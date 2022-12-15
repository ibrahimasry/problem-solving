class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        res = [0]
        i = 2
        j = 0
        n = 1 << n
        while len(res) < n:
            for k in range(len(res)-1, -1, -1):
                curr = res[k]
                res.append(curr | 1 << j)
            j += 1
        return res
        