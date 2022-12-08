class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        
    
        smallest = sum([min(r) for r in mat])
        if smallest >= target:
            return abs(target - smallest)
        prev = set()
        prev.add(0)
        for r in mat:
            curr = set()
            for n in prev:
                for m in r:
                    if n + m <= 2 * target - smallest:
                        curr.add(n + m)
            prev = curr
        return min(abs(n - target) for n in prev)