class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxn = min(nums)
        
        res = 0
        
        for n in nums:
            res += abs(n-maxn)
        return res