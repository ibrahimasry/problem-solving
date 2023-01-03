class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        spells = [[s,i] for i, s in enumerate(spells)]
        spells.sort(reverse=True)
        res = [0] * len(spells)
        j = 0
        for s, i in spells:
            while j < len(potions) and potions[j] * s < success:
                j += 1
            res[i] = len(potions ) - j
        return res
            