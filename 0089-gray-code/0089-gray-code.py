class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        prev  = [0]
        res = [0]
        i = 2
        j = 0
        n = 1 << n
        while i <= n:
            for i in range(len(res)-1, -1, -1):
                curr = res[i]
                res.append(curr | 1 << j)
                i += 1
                if len(res) == n:
                    return res
            j += 1
        return res
        