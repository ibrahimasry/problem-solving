class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        maxn = 0
        for i in range(len(nums)-2):
            maxn = max(nums[i],maxn)
            if maxn > nums[i+2]:
                return False
        return True