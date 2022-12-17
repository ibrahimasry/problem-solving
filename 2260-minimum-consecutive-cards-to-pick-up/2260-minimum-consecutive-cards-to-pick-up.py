class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = 1 + len(cards)
    
        hash = {}
        for i , n in enumerate(cards):
            if n in hash:
                res = min(res, i - hash[n]+1)
            hash[n] = i
        return -1 if res == 1 + len(cards) else res    