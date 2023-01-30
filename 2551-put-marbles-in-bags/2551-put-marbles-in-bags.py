class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        boundries = []
        for a,b in pairwise(weights):
            boundries.append(a+b)
        boundries.sort()
        
        mx = mn = 0
        for x in range(k-1):
            mn += boundries[x]
            mx += boundries[~x]
        return mx-mn