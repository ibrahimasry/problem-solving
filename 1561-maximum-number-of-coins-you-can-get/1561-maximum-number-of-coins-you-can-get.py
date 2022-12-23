class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob = len(piles)//3
        
        i = 0
        j = len(piles) - 1
        res = 0
        while i < bob:
            res += piles[j-1]
            j -= 2
            i += 1
        return res