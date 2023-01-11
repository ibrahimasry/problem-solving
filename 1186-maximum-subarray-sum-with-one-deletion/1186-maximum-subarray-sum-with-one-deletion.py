class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        res = zero = one = -inf
        for x in arr:
            one = max(zero, x + one)
            zero = max(x, x + zero)
            res = max(res, one, zero)
        return res
