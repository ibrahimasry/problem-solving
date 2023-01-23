class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = set(nums)
        count= Counter()
        res = 0
        for n in sorted(list(seen)):
            if n * n in seen:
                count[n*n] += count[n] +1
                res = max(res, count[n*n])
        return res + 1 if res >= 1 else -1
            
        
        