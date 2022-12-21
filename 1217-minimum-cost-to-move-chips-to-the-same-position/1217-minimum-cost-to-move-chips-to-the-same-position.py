class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = Counter(position)
        return min(sum([count[c] for c in count if c % 2]), sum([count[c] for c in count if c % 2 ==0]))