class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        flipped = [False] * (n+k)
        count = 0
        runningFlips = 0
        for i , curr in enumerate(nums):

            if flipped[i]:
                runningFlips -= 1

            if curr ^ (runningFlips % 2) == 0:
                if i + k > n and (curr ^ (runningFlips % 2)) == 0:
                     return -1

                count += 1
                runningFlips += 1
                flipped[i+k] = True
        return count