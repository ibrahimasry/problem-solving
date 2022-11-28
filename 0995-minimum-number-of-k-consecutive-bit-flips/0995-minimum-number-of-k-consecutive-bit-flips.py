class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        flipped = [False] * (n+k)
        count = 0
        runningFlips = 0
        for i , curr in enumerate(nums):

            if flipped[i]:
                runningFlips ^= 1

            if not curr ^ runningFlips  :
                if i + k > n :
                     return -1
                count += 1
                runningFlips ^= 1
                flipped[i+k] = True
        return count