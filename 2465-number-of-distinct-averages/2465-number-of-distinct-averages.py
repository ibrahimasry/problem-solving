class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        seen = set()
        total = sum(nums)
        nums.sort()
        n = len(nums)
        for i in range((n//2)):
            seen.add((nums[i] + nums[~i]) / 2)
        return len(seen) 