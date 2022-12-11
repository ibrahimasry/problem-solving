class Solution:
    def numSplits(self, s: str) -> int:
        right = Counter(s)
        left = Counter()
        
        
        res = 0
        
        for c in s:
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            left[c] += 1
            if len(right) == len(left):
                res += 1
        return res