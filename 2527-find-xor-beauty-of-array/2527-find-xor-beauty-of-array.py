class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda a,b: a^b, nums)