class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1
        for x,y in zip(nums,nums[1:]):
            if x > y:
                down = up + 1
            elif x < y:
                up = down + 1
        return max(up, down)