class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k * 2 > len(nums):
            return [-1] * len(nums)
        
        
        s = sum(nums[:k*2])
        ans = [-1] * len(nums)
        t = k * 2 + 1
        for i in range(k*2,len(nums)):
            s += nums[i]
            ans[i - k] = (s//t) 
            s -= nums[i - 2*k]
        return ans
            