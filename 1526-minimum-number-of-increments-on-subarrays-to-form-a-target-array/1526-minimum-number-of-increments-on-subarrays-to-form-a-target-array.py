class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        s = []
        
        res = 0
        for n in target:
            if not s :
                s.append(n)
                res += n
                continue
            if s[-1] < n:
                res += (n - s[-1])
            while s and s[-1] >= n:
                s.pop()
            s.append(n)
        return res