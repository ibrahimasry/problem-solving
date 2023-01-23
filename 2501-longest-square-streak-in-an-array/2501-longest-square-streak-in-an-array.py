class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        seen = set(nums)
        count= Counter()
        
        for n in sorted(nums):
            if n  * n in seen:
                seen.remove(n*n)
                count[n*n] += count[n] +1
                
        return max(count.values(),default=0) + 1 if max(count.values(),default=0) + 1 >= 2 else -1
            
        
        