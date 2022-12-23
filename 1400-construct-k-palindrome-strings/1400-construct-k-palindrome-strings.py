class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return  sum([c&1 for c in Counter(s).values()]) <= k <= len(s)