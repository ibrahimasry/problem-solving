class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        def maxs(arr):
            res = 0
            curr = 0
            for c in arr:
                curr = max(c, curr + c)
                res = max(curr, res)
            return res
        def mins(arr):
            res = inf
            curr = inf
            for c in arr:
                curr = min(curr + c, c)
                res = min(res, curr)
            return res
        if not any(True for n in arr if n >= 0):
            return  max(arr)
        return max(sum(arr) - mins(arr) , maxs(arr))