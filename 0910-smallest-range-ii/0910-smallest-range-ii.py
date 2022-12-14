class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        first = min(nums)
        last = max(nums)
        nums.sort()
        # Simple cases first
        res =  nums[-1] - nums[0]
        n = len(nums)
        for i in range(n-1):
            f = min(nums[i+1] - k, first+k)
            l = max(nums[i] + k, last-k)
            res = min(res, l-f)
        return res
