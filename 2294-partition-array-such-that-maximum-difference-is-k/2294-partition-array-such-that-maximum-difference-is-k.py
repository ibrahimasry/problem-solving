class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        if len(nums) == 1:
            return 1
        res = 0
        
        l = 0
        r = 0
        n = len(nums)
        while r < n:
            curr = nums[r]
            if nums[r] - nums[l] > k:
                res += 1
                l = r
            r += 1            
                
        return res + 1 