class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = high - low >> 1
        res += (1 if low % 2 or high % 2 else 0)
        return res