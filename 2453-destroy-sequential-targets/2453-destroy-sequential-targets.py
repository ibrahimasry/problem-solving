class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        
        mods = Counter([n % space for n in nums])
        maxn = max(mods.values())
        
        ans = max(nums)
        
        for n in nums:
            if mods[n % space] == maxn:
                ans = min(n, ans)
        return ans
        