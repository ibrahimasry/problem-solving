class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIdx = -1
        minVal = inf
        maxVal = -inf
        maxIdx = -1
        
        for i, v in enumerate(nums):
            if minVal > v:
                minVal = v
                minIdx = i
            if maxVal < v:
                maxVal = v
                maxIdx = i
        n = len(nums)
        
        if minIdx > maxIdx:
            minIdx, maxIdx = maxIdx, minIdx
        if minIdx == maxIdx:
            return min(minIdx+1, n-minIdx)
        return min((n-maxIdx) + minIdx+1, maxIdx+1, n-minIdx)