class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        acc = 0
        for r in range(len(nums)):
            curr = nums[r]
            acc += curr
            total = acc * (r-l+1)
            while total >= k:
                acc -= nums[l]
                l += 1
                total = acc * (r-l+1)
            res += (r-l+1)
        return res