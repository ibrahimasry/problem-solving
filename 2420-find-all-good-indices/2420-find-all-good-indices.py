class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        prefix = [1] * n
        
        for i in range(1, n):
            prefix[i] = 1 if nums[i-1] < nums[i] else prefix[i-1] + 1 
        suff = [1] * n
        
        for i in range(n-2, -1, -1):
            suff[i] = 1 if nums[i+1] < nums[i] else suff[i+1] + 1
        
        ans = []
        
        
        for i in range(k, (n-k)):
            if suff[i+1] >= k and prefix[i-1] >= k :
                ans += [i]
        return ans