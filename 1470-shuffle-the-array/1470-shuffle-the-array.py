class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2*n)
        res[::2] = nums[:n]
        res[1::2] = nums[n:]
        return res